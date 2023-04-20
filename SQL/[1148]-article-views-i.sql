-- https://leetcode.com/problems/article-views-i/

-- Write an SQL query to find all the authors that viewed at least one of their own articles.
-- Return the result table sorted by id in ascending order.
-- The query result format is in the following example.

-- Input:                                                    Output:
-- Views table:
-- +------------+-----------+-----------+------------+       +------+
-- | article_id | author_id | viewer_id | view_date  |       | id   |
-- +------------+-----------+-----------+------------+       +------+
-- | 1          | 3         | 5         | 2019-08-01 |       | 4    |
-- | 1          | 3         | 6         | 2019-08-02 |       | 7    |
-- | 2          | 7         | 7         | 2019-08-01 |       +------+
-- | 2          | 7         | 6         | 2019-08-02 |
-- | 4          | 7         | 1         | 2019-07-22 |
-- | 3          | 4         | 4         | 2019-07-21 |
-- | 3          | 4         | 4         | 2019-07-21 |
-- +------------+-----------+-----------+------------+


SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;
