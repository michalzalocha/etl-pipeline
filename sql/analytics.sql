SELECT * FROM netflix_titles;

SELECT COUNT(*) FROM netflix_titles;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'netflix_titles';

SELECT type, COUNT(*)
FROM netflix_titles
GROUP BY type;

SELECT country, COUNT(*)
FROM netflix_titles
GROUP BY country
ORDER BY COUNT(*) DESC
LIMIT 10;

SELECT release_year, COUNT(*)
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;