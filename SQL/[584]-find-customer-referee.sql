-- Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example:
-- Input:                               Output:
-- Customer table:
-- +----+------+------------+           +------+
-- | id | name | referee_id |           | name |
-- +----+------+------------+           +------+
-- | 1  | Will | null       |           | Will |
-- | 2  | Jane | null       |           | Jane |
-- | 3  | Alex | 2          |           | Bill |
-- | 4  | Bill | null       |           | Zack |
-- | 5  | Zack | 1          |           +------+
-- | 6  | Mark | 2          |
-- +----+------+------------+


SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
