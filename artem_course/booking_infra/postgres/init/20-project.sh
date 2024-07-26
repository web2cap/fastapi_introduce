#!/bin/bash

set -e


# Check required environment variables
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASS" ]; then
    echo "Error: DB_NAME, DB_USER, and DB_PASS must be set in the environment."
    exit 1
fi

# Perform all actions as $POSTGRES_USER
export PGUSER="$POSTGRES_USER"

# Create user, database, and set search_path
psql <<- EOSQL
CREATE ROLE $DB_USER WITH LOGIN;
ALTER ROLE $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASS';
CREATE DATABASE $DB_NAME OWNER $DB_USER;
EOSQL