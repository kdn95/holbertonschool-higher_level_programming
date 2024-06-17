-- Lists all records of second_table
-- List rows only with names, score before name, desc score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
