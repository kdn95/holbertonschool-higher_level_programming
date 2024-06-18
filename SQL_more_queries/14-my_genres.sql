-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
SELECT tv_genres.name
    FROM tv_genres
        -- Looking for inner join between genre_id & id in tv_genres
        JOIN tv_show_genres
            ON tv_genres.id = tv_show_genres.genre_id
                -- Making tv_show_genres.show_id equal to tv_shows.id
                WHERE tv_show_genres.show_id =
                    (SELECT id
                        FROM tv_shows
                            -- Specifically matching to "Dexter"
                            WHERE tv_shows.title="Dexter"
                    )
                    -- Ordered by genre name in ASC order
                    ORDER BY tv_genres.name ASC;
