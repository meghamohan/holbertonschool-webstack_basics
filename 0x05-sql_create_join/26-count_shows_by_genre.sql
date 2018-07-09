-- lists all genres and displays the number of shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_show_genres LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre_id ORDER BY number_shows DESC;
