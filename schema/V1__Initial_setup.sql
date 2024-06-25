CREATE KEYSPACE test_keyspace
  WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
   'replication_factor' : 1 
  };

CREATE TABLE IF NOT EXISTS test_keyspace.test_table (
    id UUID PRIMARY KEY,
    name TEXT,
    value INT
);
