CREATE KEYSPACE test_keyspace
  WITH REPLICATION = { 
   'class' : 'SimpleStrategy', 
   'replication_factor' : 1 
  };

CREATE TABLE IF NOT EXISTS test_keyspace.test_table (
    id UUID PRIMARY KEY,
    name TEXT,
    value INT
    age INT
    others INT
    others2 INT
    others3 INT
    others4 INT
    others5 INT
    others6 INT
    others7 INT
    others8 INT
    others9 INT
);
