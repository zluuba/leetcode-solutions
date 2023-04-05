-- Write an SQL query to report the names of all the salespersons who did not have any orders related to the company
-- with the name "RED".
-- Return the result table in any order.

-- Example:
-- Input:
-- SalesPerson table:                                                  Company table:
-- +----------+------+--------+-----------------+------------+         +--------+--------+----------+
-- | sales_id | name | salary | commission_rate | hire_date  |         | com_id | name   | city     |
-- +----------+------+--------+-----------------+------------+         +--------+--------+----------+
-- | 1        | John | 100000 | 6               | 4/1/2006   |         | 1      | RED    | Boston   |
-- | 2        | Amy  | 12000  | 5               | 5/1/2010   |         | 2      | ORANGE | New York |
-- | 3        | Mark | 65000  | 12              | 12/25/2008 |         | 3      | YELLOW | Boston   |
-- | 4        | Pam  | 25000  | 25              | 1/1/2005   |         | 4      | GREEN  | Austin   |
-- | 5        | Alex | 5000   | 10              | 2/3/2007   |         +--------+--------+----------+
-- +----------+------+--------+-----------------+------------+
-- Orders table:                                                       Output:
-- +----------+------------+--------+----------+--------+              +------+
-- | order_id | order_date | com_id | sales_id | amount |              | name |
-- +----------+------------+--------+----------+--------+              +------+
-- | 1        | 1/1/2014   | 3      | 4        | 10000  |              | Amy  |
-- | 2        | 2/1/2014   | 4      | 5        | 5000   |              | Mark |
-- | 3        | 3/1/2014   | 1      | 1        | 50000  |              | Alex |
-- | 4        | 4/1/2014   | 1      | 4        | 25000  |              +------+
-- +----------+------------+--------+----------+--------+
-- Explanation:
-- According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales
-- to company RED, so we report all the other names in the table salesperson.


SELECT SalesPerson.name FROM SalesPerson
    WHERE SalesPerson.name NOT IN (
        SELECT SalesPerson.name FROM SalesPerson
            LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
            LEFT JOIN Company ON Orders.com_id = Company.com_id
                WHERE Company.name = 'RED'
    );


-- Alternative solution
SELECT SalesPerson.name FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (
    SELECT Orders.sales_id FROM Orders
    WHERE Orders.com_id IN (
        SELECT Company.com_id FROM Company
        WHERE Company.name = 'RED'
    )
);
