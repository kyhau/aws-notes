# psql and alembic

```
################################################################################
# PSQL

psql --host=xxx.xxx.ap-southeast-2.rds.amazonaws.com --port=5432 --username=xxx --dbname=unit_tests

# List all databases
psql:  \list

# List all databases
psql:  SELECT datname FROM pg_database WHERE datistemplate = false;

# Switch database
psql:  \connect database_name

# List all users
psql:  \du  (or  \dg)

# Drop user
DROP USER name

# List all extensions
psql:  \dx

# List all schemas and tables
psql:
SELECT table_schema,table_name FROM information_schema.tables ORDER BY table_schema,table_name;

# List default specfic schema (i.e. 'public')'s tables
psql:  
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;

SELECT * from groups;
SELECT * from users;

# Re-create default schema 'public' (i.e. drop all tables, functions, views, etc in 'public') 
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';

# Show all schema
psql:  select * from information_schema.schemata;

# Exit psql
psql:  \q


################################################################################
# alembic

sudo apt-get install alembic
cd repo_folder/
alembic --config config/production.ini upgrade head

# Alembic stores the version history in your database. Hence it is using the value stored in your database to search
# for the revision. The version number for my personal database is stored in the table alembic_version

SELECT * FROM alembic_version;

# If you got error: Can't locate revision identified by 'xxxxxx'

SELECT * FROM alembic_version;
DROP TABLE alembic_version;
alembic -c config/development.ini upgrade head 


################################################################################
# The default postgre user

# 1. To reset postgres password (quickest)
sudo su postgres
psql -U postgres
\password
\q

# 2. To login as postgres and delete user 
# Case (1): postgres is in 'peer' mode, i.e. can connect locally only.

psql --username=postgres -h 127.0.0.1

```