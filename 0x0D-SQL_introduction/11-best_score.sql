-- script that lists all records of the table second_table where score >= 10.
-- Records is ordered by score (top first)

SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
