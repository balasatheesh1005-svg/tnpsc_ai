import os
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    rows = supabase.table("user_revisions").select("*").limit(1).execute()
    print("ROW_RESPONSE:", rows.data if hasattr(rows, "data") else rows)
except Exception as e:
    print("ROW_ERROR:", repr(e))

try:
    meta = (
        supabase.table("information_schema.columns")
        .select(
            "column_name,data_type,is_nullable,character_maximum_length,numeric_precision"
        )
        .eq("table_name", "user_revisions")
        .execute()
    )
    print("META_RESPONSE:", meta.data if hasattr(meta, "data") else meta)
except Exception as e:
    print("META_ERROR:", repr(e))
