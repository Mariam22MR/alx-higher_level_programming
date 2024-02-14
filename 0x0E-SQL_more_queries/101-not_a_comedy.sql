-- Prints records with column values in set formed
-- from intersection of multiple tables
SELECT tv_shows.title FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
AND tv_show_genres.genre_id = (
	SELECT id FROM tv_genres
	WHERE name = 'Comedy')
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
