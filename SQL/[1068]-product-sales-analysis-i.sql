-- https://leetcode.com/problems/product-sales-analysis-i/

-- Write an SQL query that reports the product_name, year, and price for each sale_id in the Sales table.
-- Return the resulting table in any order.

-- Example:
-- Input:
-- Sales table:                                            Product table:
-- +---------+------------+------+----------+-------+      +------------+--------------+
-- | sale_id | product_id | year | quantity | price |      | product_id | product_name |
-- +---------+------------+------+----------+-------+      +------------+--------------+
-- | 1       | 100        | 2008 | 10       | 5000  |      | 100        | Nokia        |
-- | 2       | 100        | 2009 | 12       | 5000  |      | 200        | Apple        |
-- | 7       | 200        | 2011 | 15       | 9000  |      | 300        | Samsung      |
-- +---------+------------+------+----------+-------+      +------------+--------------+
-- Output:
-- +--------------+-------+-------+
-- | product_name | year  | price |
-- +--------------+-------+-------+
-- | Nokia        | 2008  | 5000  |
-- | Nokia        | 2009  | 5000  |
-- | Apple        | 2011  | 9000  |
-- +--------------+-------+-------+
-- Explanation:
-- From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
-- From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
-- From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.


SELECT Product.product_name, Sales.year, Sales.price
FROM Product, Sales
WHERE Product.product_id = Sales.product_id;

-- Alternative solution

SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
LEFT JOIN Product ON Product.product_id = Sales.product_id;
