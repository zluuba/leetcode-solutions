-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.

-- Example:
-- Input:                                           Output:
-- Customers table:     Orders table:
-- +----+-------+       +----+------------+         +-----------+
-- | id | name  |       | id | customerId |         | Customers |
-- +----+-------+       +----+------------+         +-----------+
-- | 1  | Joe   |       | 1  | 3          |         | Henry     |
-- | 2  | Henry |       | 2  | 1          |         | Max       |
-- | 3  | Sam   |       +----+------------+         +-----------+
-- | 4  | Max   |
-- +----+-------+


SELECT Customers.name AS Customers
FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerId
WHERE Orders.id IS NULL;
