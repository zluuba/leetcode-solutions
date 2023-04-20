-- https://leetcode.com/problems/rearrange-products-table/

-- Write an SQL query to rearrange the Products table so that each row has (product_id, store, price).
-- If a product is not available in a store, do not include a row with that product_id and
-- store combination in the result table.
-- Return the result table in any order.

-- Example:
-- Input:
-- Products table:
-- +------------+--------+--------+--------+
-- | product_id | store1 | store2 | store3 |
-- +------------+--------+--------+--------+
-- | 0          | 95     | 100    | 105    |
-- | 1          | 70     | null   | 80     |
-- +------------+--------+--------+--------+
-- Output:
-- +------------+--------+-------+
-- | product_id | store  | price |
-- +------------+--------+-------+
-- | 0          | store1 | 95    |
-- | 0          | store2 | 100   |
-- | 0          | store3 | 105   |
-- | 1          | store1 | 70    |
-- | 1          | store3 | 80    |
-- +------------+--------+-------+
-- Explanation:
-- Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
-- Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.


SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL

UNION ALL

SELECT product_id, 'store2', store2
FROM Products
WHERE store2 IS NOT NULL

UNION ALL

SELECT product_id, 'store3', store3
FROM Products
WHERE store3 IS NOT NULL;


-- Alternative solution

SELECT
    prod.product_id,
    prod.store,
    prod.price
FROM (
    SELECT product_id, 'store1' AS store, store1 AS price FROM Products
    UNION ALL
    SELECT product_id, 'store2', store2 FROM Products
    UNION ALL
    SELECT product_id, 'store3', store3 FROM Products
) AS prod
WHERE prod.price IS NOT NULL;
