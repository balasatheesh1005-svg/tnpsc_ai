"""Server-side staging identity binding for the future Streamlit callback."""

from dataclasses import dataclass, field
from uuid import UUID

from supabase import ClientOptions, create_client

from core.firebase_token_validation import FirebaseGoogleTokenValidator
from core.staging_config import get_staging_config

FIREBASE_PROJECT = "tnpsc-nova-ai-auth-test"
SUPABASE_PROJECT = "fcuykyzgmnwoevmvibbu"


class FirebaseProfileBindingError(ValueError):
    """The Firebase identity could not be bound to an existing staging profile."""


@dataclass(frozen=True)
class FirebaseProfileBinding:
    profile_id: UUID
    expires_at: int
    client: object = field(repr=False)


def bind_firebase_profile(token: str) -> FirebaseProfileBinding:
    """Resolve a previously provisioned profile through the user's own RLS context.

    Callers must keep the resulting client in a single Streamlit session and
    discard it at logout or expiry. This function does not establish a UI session.
    """
    config = get_staging_config()
    if (
        config.project_ref != SUPABASE_PROJECT
        or config.supabase_url != f"https://{SUPABASE_PROJECT}.supabase.co"
    ):
        raise FirebaseProfileBindingError("Firebase binding requires the pinned test database.")

    identity = FirebaseGoogleTokenValidator(FIREBASE_PROJECT).validate(token)
    try:
        client = create_client(
            config.supabase_url,
            config.supabase_key,
            options=ClientOptions(auto_refresh_token=False, persist_session=False),
        )
        client.postgrest.auth(token)
        # Do not accept a UUID or email from the callback. The staging policy
        # resolves the verified JWT subject through the private identity map.
        linked_id = UUID(client.rpc("get_linked_firebase_profile_id").execute().data)
        profiles = client.table("profiles").select("id").limit(2).execute().data
        if len(profiles) != 1 or UUID(profiles[0]["id"]) != linked_id:
            raise ValueError()
        return FirebaseProfileBinding(linked_id, identity.expires_at, client)
    except Exception:
        raise FirebaseProfileBindingError("Unable to resolve a linked staging profile.") from None
