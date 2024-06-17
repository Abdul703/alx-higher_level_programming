-- Script that creates a table called first_table in the current database in your MySQL server.
-- If the table already exist, the script will not fail

-- creating new table 'first_table'
CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
