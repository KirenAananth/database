CREATE KEYSPACE IF NOT EXISTS dbaas_common WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS dbaas_common.new_table (
    id UUID PRIMARY KEY,
    name text,
    created_at timestamp
);

