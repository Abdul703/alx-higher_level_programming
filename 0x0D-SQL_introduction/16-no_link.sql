-- script that lists all records of the table second_table where name is not null.
-- Records is ordered by score (top first)

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
