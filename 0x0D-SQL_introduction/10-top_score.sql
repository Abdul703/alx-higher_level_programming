-- script that lists all records of the table second_table of a database in MySQL server.
-- Records is ordered by score (top first)

SELECT score, name FROM second_table ORDER BY score DESC;
