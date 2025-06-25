-- Lista de todos los registros con puntuacion mayor o igual a diez
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
