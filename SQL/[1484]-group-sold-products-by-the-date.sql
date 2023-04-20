-- https://leetcode.com/problems/group-sold-products-by-the-date/

-- Write an SQL query to find for each date the number of different products sold and their names.
-- The sold products names for each date should be sorted lexicographically.
-- Return the result table ordered by sell_date.

-- Example:
-- Input:                              Output:
-- Activities table:
-- +------------+------------+         +------------+----------+------------------------------+
-- | sell_date  | product     |        | sell_date  | num_sold | products                     |
-- +------------+------------+         +------------+----------+------------------------------+
-- | 2020-05-30 | Headphone  |         | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
-- | 2020-06-01 | Pencil     |         | 2020-06-01 | 2        | Bible,Pencil                 |
-- | 2020-06-02 | Mask       |         | 2020-06-02 | 1        | Mask                         |
-- | 2020-05-30 | Basketball |         +------------+----------+------------------------------+
-- | 2020-06-01 | Bible      |
-- | 2020-06-02 | Mask       |
-- | 2020-05-30 | T-Shirt    |
-- +------------+------------+
-- Explanation:
-- For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
-- For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
-- For 2020-06-02, the Sold item is (Mask), we just return it.


SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
