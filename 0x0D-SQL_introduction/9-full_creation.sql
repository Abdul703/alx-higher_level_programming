-- script that creates a table second_table in the database hbtn_0c_0 in MySQL server and add multiples rows.

-- table creation
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

-- adding rows
INSERT INTO second_table (id, name, score) VALUE (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUE (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUE (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUE (4, "George", 8);
