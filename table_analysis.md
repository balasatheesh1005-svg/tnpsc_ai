# TNPSC Nova AI — Identity Migration v1.0
## Detailed Table Analysis & Risk Assessment Document

**Architect:** Lead Database Architect, TNPSC Nova AI  
**Date:** July 23, 2026  
**Document Version:** 1.0  

---

## 1. Comprehensive Schema Comparison

This section provides line-by-line structural comparisons between the **Current Schema** and the **Target Schema (Phase 1)** for all user-related tables in TNPSC Nova AI.

---

### 1.1. Table: `profiles`

#### Current Schema
```sql
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
-- Schema remains structurally unchanged in Phase 1.
-- Acts as the reference parent table for all user_id Foreign Keys.
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

### 1.2. Table: `users_progress`

#### Current Schema
```sql
CREATE TABLE public.users_progress (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    total_questions INTEGER DEFAULT 0,
    correct_answers INTEGER DEFAULT 0,
    accuracy DOUBLE PRECISION DEFAULT 0.0,
    subject TEXT,
    topic TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.users_progress (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    total_questions INTEGER DEFAULT 0,
    correct_answers INTEGER DEFAULT 0,
    accuracy DOUBLE PRECISION DEFAULT 0.0,
    subject TEXT,
    topic TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_users_progress_user_id ON public.users_progress(user_id);
```

---

### 1.3. Table: `user_xp`

#### Current Schema
```sql
CREATE TABLE public.user_xp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE NOT NULL,
    xp INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.user_xp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    xp INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_user_xp_user_id ON public.user_xp(user_id);
```

---

### 1.4. Table: `users_weakness`

#### Current Schema
```sql
CREATE TABLE public.users_weakness (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    subject TEXT,
    topic TEXT,
    weakness INTEGER DEFAULT 1,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.users_weakness (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    subject TEXT,
    topic TEXT,
    weakness INTEGER DEFAULT 1,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_users_weakness_user_id ON public.users_weakness(user_id);
```

---

### 1.5. Table: `user_revisions`

#### Current Schema
```sql
CREATE TABLE public.user_revisions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    subject TEXT,
    topic TEXT,
    next_revision TIMESTAMP WITH TIME ZONE,
    interval INTEGER DEFAULT 1,
    ease_factor DOUBLE PRECISION DEFAULT 2.5,
    repetitions INTEGER DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.user_revisions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    subject TEXT,
    topic TEXT,
    next_revision TIMESTAMP WITH TIME ZONE,
    interval INTEGER DEFAULT 1,
    ease_factor DOUBLE PRECISION DEFAULT 2.5,
    repetitions INTEGER DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_user_revisions_user_id ON public.user_revisions(user_id);
```

---

### 1.6. Table: `user_streaks`

#### Current Schema
```sql
CREATE TABLE public.user_streaks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    streak INTEGER DEFAULT 0,
    max_streak INTEGER DEFAULT 0,
    last_activity_date DATE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.user_streaks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    streak INTEGER DEFAULT 0,
    max_streak INTEGER DEFAULT 0,
    last_activity_date DATE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_user_streaks_user_id ON public.user_streaks(user_id);
```

---

### 1.7. Table: `daily_missions`

#### Current Schema
```sql
CREATE TABLE public.daily_missions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    daily_test_completed BOOLEAN DEFAULT FALSE,
    pyq_solved INTEGER DEFAULT 0,
    revision_completed BOOLEAN DEFAULT FALSE,
    streak_days INTEGER DEFAULT 0,
    date DATE DEFAULT CURRENT_DATE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.daily_missions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    daily_test_completed BOOLEAN DEFAULT FALSE,
    pyq_solved INTEGER DEFAULT 0,
    revision_completed BOOLEAN DEFAULT FALSE,
    streak_days INTEGER DEFAULT 0,
    date DATE DEFAULT CURRENT_DATE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_daily_missions_user_id ON public.daily_missions(user_id);
```

---

### 1.8. Table: `mentor_memory`

#### Current Schema
```sql
CREATE TABLE public.mentor_memory (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    memory_data JSONB DEFAULT '{}'::jsonb,
    summary TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.mentor_memory (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    memory_data JSONB DEFAULT '{}'::jsonb,
    summary TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_mentor_memory_user_id ON public.mentor_memory(user_id);
```

---

### 1.9. Table: `bookmarks`

#### Current Schema
```sql
CREATE TABLE public.bookmarks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    question_id TEXT NOT NULL,
    topic TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.bookmarks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    question_id TEXT NOT NULL,
    topic TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_bookmarks_user_id ON public.bookmarks(user_id);
```

---

### 1.10. Table: `user_analytics`

#### Current Schema
```sql
CREATE TABLE public.user_analytics (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    action TEXT NOT NULL,
    payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Target Schema (Phase 1)
```sql
CREATE TABLE public.user_analytics (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE, -- [NEW NULLABLE COLUMN]
    action TEXT NOT NULL,
    payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_user_analytics_user_id ON public.user_analytics(user_id);
```

---

## 2. Comprehensive Risk Analysis

### Risk 1: Table Lock & DDL Execution Overhead
- **Assessment**: Adding a column in PostgreSQL without a default value or with `NULL` default takes `ACCESS EXCLUSIVE` lock for only a fraction of a millisecond because it updates catalog metadata without re-writing table pages.
- **Mitigation**: Executed via transaction block in `identity_migration_phase1.sql`. Zero downtime.

### Risk 2: Existing Application Compatibility
- **Assessment**: Current Python queries issue SELECT / INSERT / UPDATE / UPSERT statements using `username` column filters (e.g., `.eq("username", username)`).
- **Mitigation**: `username` columns remain unaltered. `user_id` is initialized as NULLABLE, meaning existing inserts ignoring `user_id` will succeed without error.

### Risk 3: Premature FK Constraint Enforcement
- **Assessment**: If `NOT NULL` or mandatory FK checks were enforced immediately, any row inserted without `user_id` would fail.
- **Mitigation**: `user_id` columns are strictly NULLABLE in Phase 1. FK constraints enforce integrity only when a non-null `user_id` is written.

### Risk 4: Index Overhead
- **Assessment**: Adding non-unique indexes (`idx_*_user_id`) consumes minor storage and has negligible write overhead.
- **Mitigation**: Indexes use standard btree indexing on 16-byte UUID types, offering maximum read performance for Phase 2 query migration.

---

## 3. Rollback Plan

If Phase 1 needs to be completely reverted for any operational reason, run the following safe DDL rollback commands in the Supabase SQL Editor. This will remove the `user_id` columns and indexes without modifying any operational `username` data or user progress.

```sql
BEGIN;

-- Drop added indexes
DROP INDEX IF EXISTS public.idx_users_progress_user_id;
DROP INDEX IF EXISTS public.idx_user_xp_user_id;
DROP INDEX IF EXISTS public.idx_users_weakness_user_id;
DROP INDEX IF EXISTS public.idx_user_revisions_user_id;
DROP INDEX IF EXISTS public.idx_user_streaks_user_id;
DROP INDEX IF EXISTS public.idx_daily_missions_user_id;
DROP INDEX IF EXISTS public.idx_mentor_memory_user_id;
DROP INDEX IF EXISTS public.idx_bookmarks_user_id;
DROP INDEX IF EXISTS public.idx_user_analytics_user_id;

-- Drop added user_id columns
ALTER TABLE public.users_progress DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.user_xp DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.users_weakness DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.user_revisions DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.user_streaks DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.daily_missions DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.mentor_memory DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.bookmarks DROP COLUMN IF EXISTS user_id;
ALTER TABLE public.user_analytics DROP COLUMN IF EXISTS user_id;

COMMIT;
```

---

## 4. Phase 1 Migration & Validation Checklist

### Pre-Migration Checks
- [x] Verify database connectivity via Supabase SQL Editor or client.
- [x] Audit all Python files (`core/*.py`) to confirm zero dependencies on `user_id` presence during Phase 1.
- [x] Confirm backup or point-in-time recovery is active in Supabase.

### Execution Steps
- [ ] Run `identity_migration_phase1.sql` in the Supabase SQL Console.
- [ ] Confirm `COMMIT` executed without errors.

### Post-Migration Validation SQL
Run the following SQL verification snippet to confirm schema readiness:

```sql
SELECT 
    t.table_name,
    c.column_name,
    c.data_type,
    c.is_nullable
FROM 
    information_schema.tables t
LEFT JOIN 
    information_schema.columns c 
    ON t.table_name = c.table_name 
    AND c.column_name = 'user_id'
WHERE 
    t.table_schema = 'public'
    AND t.table_name IN (
        'profiles', 'users_progress', 'user_xp', 'users_weakness',
        'user_revisions', 'user_streaks', 'daily_missions',
        'mentor_memory', 'bookmarks', 'user_analytics'
    )
ORDER BY 
    t.table_name;
```

### Readiness Sign-Off for Phase 2
- [ ] All 10 user-related tables reflect `user_id` (UUID, nullable).
- [ ] All Python tests and Streamlit application functionality operate with 100% success.
- [ ] Database is ready for Phase 2 (Data Migration & Dual-Write Engine).
