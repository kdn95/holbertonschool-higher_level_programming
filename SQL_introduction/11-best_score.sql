-- Lists all records with score >= 10 in second table
-- Should show score then name and ordered by top score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;