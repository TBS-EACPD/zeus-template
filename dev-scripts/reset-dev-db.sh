#!/bin/bash

# run this as source reset_dev_db.sh path_to_sql_dump.sql 
source ./dev-scripts/write-envs.sh



dropdb $DB_NAME;
createdb $DB_NAME;
psql "dbname=$DB_NAME" < $1;

# this is necessary for django to connect 
psql --dbname="$DB_NAME" -c "GRANT CONNECT ON DATABASE \"$DB_NAME\" TO \"$DB_USERNAME\";"
psql --dbname="$DB_NAME" -c "GRANT USAGE ON SCHEMA public TO \"$DB_USERNAME\";"
psql --dbname="$DB_NAME" -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"$DB_USERNAME\";"
psql --dbname="$DB_NAME" -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO \"$DB_USERNAME\";"

for tbl in `psql --dbname="$DB_NAME" -qAt -c "select tablename from pg_tables where schemaname = 'public';"`;
    do  psql --dbname="$DB_NAME" -c "alter table \"$tbl\" owner to \"$DB_USERNAME\";";
done

echo "done";