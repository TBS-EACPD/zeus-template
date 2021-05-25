source dev-scripts/write-envs.sh
pg_dump -U $DB_USERNAME --format=plain --no-owner --no-acl $DB_NAME