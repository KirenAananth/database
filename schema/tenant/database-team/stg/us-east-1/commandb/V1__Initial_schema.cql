CREATE KEYSPACE dbaas_common WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE dbaas_common.test_data (
    id UUID PRIMARY KEY,
    name text,
    age int,
    email text
);

