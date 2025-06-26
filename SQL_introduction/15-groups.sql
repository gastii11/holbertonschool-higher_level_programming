-- Enumera el numero de registros con la misma puntuacion
SELECT score, COUNT(*) AS number_of_records
FROM second_table
GROUP BY score;
ORDER BY number_of_records DESC;
