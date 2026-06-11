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

-- PHASE 5: XP + LEVEL SYSTEM
-- core/xp_ai.py:
-- supabase.table("user_xp").upsert(..., on_conflict="username")

-- Create table if not exists
create table if not exists public.user_xp (
  id uuid primary key default uuid_generate_v4(),
  username text not null unique,
  xp integer not null default 0,
  level integer not null default 1,
  updated_at timestamp with time zone default now()
);

-- Check and add unique constraint for username
do $$
begin
  if not exists (
    select 1
    from pg_constraint
    where conname = 'user_xp_username_key'
  ) then
    alter table public.user_xp
      add constraint user_xp_username_key
      unique (username);
  end if;
end $$;

-- Create index for faster lookups
create index if not exists idx_user_xp_username on public.user_xp(username);
create index if not exists idx_user_xp_level on public.user_xp(level);
