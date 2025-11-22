# Write your MySQL query statement below
SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC # We can choose to add ASC but by default it is already ascending.