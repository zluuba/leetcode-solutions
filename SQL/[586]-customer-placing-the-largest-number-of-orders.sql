-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.

-- Example:
-- Input:                                      Output:
-- Orders table:
-- +--------------+-----------------+          +-----------------+
-- | order_number | customer_number |          | customer_number |
-- +--------------+-----------------+          +-----------------+
-- | 1            | 1               |          | 3               |
-- | 2            | 2               |          +-----------------+
-- | 3            | 3               |
-- | 4            | 3               |
-- +--------------+-----------------+
-- Explanation:
-- The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order.
-- So the result is customer_number 3.


SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
