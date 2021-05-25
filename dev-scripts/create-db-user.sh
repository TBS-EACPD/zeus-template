source ./dev-scripts/write-envs.sh
psql -c "CREATE ROLE \"$DB_USERNAME\" with login"
psql -c "alter user \"$DB_USERNAME\" createdb";