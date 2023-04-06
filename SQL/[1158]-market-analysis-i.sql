-- Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.
-- Return the result table in any order.

-- Example:
-- Input:
-- Users table:                                Orders table:
-- +---------+------------+----------------+   +----------+------------+---------+----------+-----------+
-- | user_id | join_date  | favorite_brand |   | order_id | order_date | item_id | buyer_id | seller_id |
-- +---------+------------+----------------+   +----------+------------+---------+----------+-----------+
-- | 1       | 2018-01-01 | Lenovo         |   | 1        | 2019-08-01 | 4       | 1        | 2         |
-- | 2       | 2018-02-09 | Samsung        |   | 2        | 2018-08-02 | 2       | 1        | 3         |
-- | 3       | 2018-01-19 | LG             |   | 3        | 2019-08-03 | 3       | 2        | 3         |
-- | 4       | 2018-05-21 | HP             |   | 4        | 2018-08-04 | 1       | 4        | 2         |
-- +---------+------------+----------------+   | 5        | 2018-08-04 | 1       | 3        | 4         |
--                                             | 6        | 2019-08-05 | 2       | 2        | 4         |
--                                             +----------+------------+---------+----------+-----------+
-- Items table:                                Output:
-- +---------+------------+                    +-----------+------------+----------------+
-- | item_id | item_brand |                    | buyer_id  | join_date  | orders_in_2019 |
-- +---------+------------+                    +-----------+------------+----------------+
-- | 1       | Samsung    |                    | 1         | 2018-01-01 | 1              |
-- | 2       | Lenovo     |                    | 2         | 2018-02-09 | 2              |
-- | 3       | LG         |                    | 3         | 2018-01-19 | 0              |
-- | 4       | HP         |                    | 4         | 2018-05-21 | 0              |
-- +---------+------------+                    +-----------+------------+----------------+


SELECT
    Users.user_id AS buyer_id,
    Users.join_date,
    SUM(
        IF(YEAR(Orders.order_date) = 2019, 1, 0)
    ) AS orders_in_2019
FROM Users
LEFT JOIN Orders ON Users.user_id = Orders.buyer_id
GROUP BY Users.user_id;
