-- Script that creates a table called force_name in the current database in your MySQL server.
-- If the table already exist, the script will not fail

-- creating new table 'force_name'
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
