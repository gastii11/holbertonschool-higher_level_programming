-- Enumera tdas las ciudades de california
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id FROM state WHERE name = 'california'
)
ORDER BY cities.id ASC;
