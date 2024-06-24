-- Script that creates a table called id_not_null in the current database in your MySQL server.
-- If the table already exist, the script will not fail

-- creating new table 'id_not_null'
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
