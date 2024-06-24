-- Script that creates a table called unique_id in the current database in your MySQL server.
-- If the table already exist, the script will not fail

-- creating new table 'unique_id'
CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
