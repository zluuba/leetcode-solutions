-- https://leetcode.com/problems/bank-account-summary-ii/

-- Write an SQL query to report the name and balance of users with a balance higher than 10000.
-- The balance of an account is equal to the sum of the amounts of all transactions involving that account.
-- Return the result table in any order.

-- Example:
-- Input:
-- Transactions table:                                             Users table:
-- +------------+------------+------------+---------------+        +------------+--------------+
-- | trans_id   | account    | amount     | transacted_on |        | account    | name         |
-- +------------+------------+------------+---------------+        +------------+--------------+
-- | 1          | 900001     | 7000       |  2020-08-01   |        | 900001     | Alice        |
-- | 2          | 900001     | 7000       |  2020-09-01   |        | 900002     | Bob          |
-- | 3          | 900001     | -3000      |  2020-09-02   |        | 900003     | Charlie      |
-- | 4          | 900002     | 1000       |  2020-09-12   |        +------------+--------------+
-- | 5          | 900003     | 6000       |  2020-08-07   |
-- | 6          | 900003     | 6000       |  2020-09-07   |
-- | 7          | 900003     | -4000      |  2020-09-11   |
-- +------------+------------+------------+---------------+
-- Output:
-- +------------+------------+
-- | name       | balance    |
-- +------------+------------+
-- | Alice      | 11000      |
-- +------------+------------+
-- Explanation:
-- Alice's balance is (7000 + 7000 - 3000) = 11000.
-- Bob's balance is 1000.
-- Charlie's balance is (6000 + 6000 - 4000) = 8000.


SELECT
    Users.name AS NAME,
    SUM(Transactions.amount) AS BALANCE
FROM Users
LEFT JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.name
HAVING balance > 10000;
