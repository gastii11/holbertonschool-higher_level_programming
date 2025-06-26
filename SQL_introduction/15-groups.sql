-- Enumera el numero de registros con la misma puntuacion
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
