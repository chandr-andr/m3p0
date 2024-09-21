IS_TABLE_EXISTS_QUERY = """
SELECT EXISTS (
    SELECT FROM information_schema.tables 
    WHERE  table_schema = 'public'
    AND    table_name   = 'c3pg0_migrations'
)
"""

CREATE_TABLE_QUERY = """
CREATE TABLE c3pg0_migrations (
    id SERIAL,
    version VARCHAR,
    revision UUID
)
"""

IS_VERSION_ALREADY_EXIST = """
SELECT EXISTS (
    SELECT version 
    FROM c3pg0
    WHERE version = $1
)
"""

RETRIEVE_LAST_REVISION = """
SELECT revision
FROM c3pg0_migrations
ORDER BY id DESC
LIMIT 1
"""

RETRIEVE_SORTED_REVISIONS = """
SELECT revision
FROM c3pg0_migrations
ORDER BY id DESC
"""
