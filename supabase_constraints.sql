-- Supabase constraints required by Python upsert(on_conflict=...)
-- Run the duplicate checks first. If they return rows, clean those duplicates
-- before adding the unique constraints.

-- core/revision_ai.py:
-- supabase.table("user_revisions").upsert(..., on_conflict="username,subject,topic")
select username, subject, topic, count(*) as duplicate_count
from public.user_revisions
group by username, subject, topic
having count(*) > 1;

do $$
begin
  if not exists (
    select 1
    from pg_constraint
    where conname = 'user_revisions_username_subject_topic_key'
  ) then
    alter table public.user_revisions
      add constraint user_revisions_username_subject_topic_key
      unique (username, subject, topic);
  end if;
end $$;

-- core/mentor_memory.py:
-- supabase.table("mentor_memory").upsert(..., on_conflict="username")
select username, count(*) as duplicate_count
from public.mentor_memory
group by username
having count(*) > 1;

do $$
begin
  if not exists (
    select 1
    from pg_constraint
    where conname = 'mentor_memory_username_key'
  ) then
    alter table public.mentor_memory
      add constraint mentor_memory_username_key
      unique (username);
  end if;
end $$;
