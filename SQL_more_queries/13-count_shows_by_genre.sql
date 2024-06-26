-- Write a script that lists all genres from hbtn_0d_tvshows and 
-- displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre> - D
-- First column must be called genre - D
-- Second column must be called number_of_shows - D
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT name AS genre, COUNT(show_id) AS number_of_shows
    FROM tv_genres
        INNER JOIN tv_show_genres
            ON tv_genres.id = tv_show_genres.genre_id
                GROUP BY name
                    ORDER BY number_of_shows DESC;
