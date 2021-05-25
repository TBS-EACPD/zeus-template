source ./dev-scripts/write-envs.sh
createdb $TEST_DB_NAME

# this is necessary for django to connect 
psql --dbname="$TEST_DB_NAME" -c "GRANT CONNECT ON DATABASE \"$TEST_DB_NAME\" TO \"$DB_USERNAME\";"
psql --dbname="$TEST_DB_NAME" -c "GRANT USAGE ON SCHEMA public TO \"$DB_USERNAME\";"
psql --dbname="$TEST_DB_NAME" -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO \"$DB_USERNAME\";"
psql --dbname="$TEST_DB_NAME" -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO \"$DB_USERNAME\";"

for tbl in `psql --dbname="$TEST_DB_NAME" -qAt -c "select tablename from pg_tables where schemaname = 'public';"`;
    do  psql --dbname="$TEST_DB_NAME" -c "alter table \"$tbl\" owner to \"$DB_USERNAME\";";
done
