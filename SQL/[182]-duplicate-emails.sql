-- https://leetcode.com/problems/duplicate-emails/

-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.

-- Example:
-- Input:                  Output:
-- Person table:
-- +----+---------+        +---------+
-- | id | email   |        | Email   |
-- +----+---------+        +---------+
-- | 1  | a@b.com |        | a@b.com |
-- | 2  | c@d.com |        +---------+
-- | 3  | a@b.com |
-- +----+---------+
-- Explanation: a@b.com is repeated two times.


SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
