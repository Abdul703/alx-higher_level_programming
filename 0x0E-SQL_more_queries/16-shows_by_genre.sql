-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, name;
