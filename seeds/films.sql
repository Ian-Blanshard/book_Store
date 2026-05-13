DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO films (title, release_year) VALUES ('Dune Part I', 2021);
INSERT INTO films (title, release_year) VALUES ('Dune Part II', 2024);
INSERT INTO films (title, release_year) VALUES ('Serenity', 2005);
