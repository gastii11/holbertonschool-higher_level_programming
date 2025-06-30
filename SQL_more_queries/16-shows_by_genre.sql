-- Lista todos los programas y todos los generos vinvulados
SELECT tv_show.title, tv_genres.name
FROM tv_show
LEFT JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_show.title ASC, tv_genres.name ASC;
