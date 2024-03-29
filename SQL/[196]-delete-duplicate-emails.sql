-- https://leetcode.com/problems/delete-duplicate-emails/

-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.
-- Note that you are supposed to write a DELETE statement and not a SELECT one.
-- After running your script, the answer shown is the Person table.
-- The driver will first compile and run your piece of code and then show the Person table.
-- The final order of the Person table does not matter.

-- Example:
-- Input:                              Output:
-- Person table:
-- +----+------------------+           +----+------------------+
-- | id | email            |           | id | email            |
-- +----+------------------+           +----+------------------+
-- | 1  | john@example.com |           | 1  | john@example.com |
-- | 2  | bob@example.com  |           | 2  | bob@example.com  |
-- | 3  | john@example.com |           +----+------------------+
-- +----+------------------+
-- Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
-- Please write a DELETE statement and DO NOT write a SELECT statement.


DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;
