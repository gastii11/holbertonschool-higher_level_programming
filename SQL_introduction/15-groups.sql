-- Enumera el numero de registros con la misma puntuacion
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
