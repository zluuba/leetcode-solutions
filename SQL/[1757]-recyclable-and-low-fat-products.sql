-- Write an SQL query to find the ids of products that are both low fat and recyclable.
-- Return the result table in any order.

-- Example:
-- Input:                                          Output:
-- Products table:
-- +-------------+----------+------------+         +-------------+
-- | product_id  | low_fats | recyclable |         | product_id  |
-- +-------------+----------+------------+         +-------------+
-- | 0           | Y        | N          |         | 1           |
-- | 1           | Y        | Y          |         | 3           |
-- | 2           | N        | Y          |         +-------------+
-- | 3           | Y        | Y          |
-- | 4           | N        | N          |
-- +-------------+----------+------------+
-- Explanation: Only products 1 and 3 are both low fat and recyclable.


SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
