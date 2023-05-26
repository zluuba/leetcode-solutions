-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

-- Write an SQL query to show the unique ID of each user, If a user does not have a unique ID replace just show null.
-- Return the result table in any order.

-- Example:
-- Input:                                              Output:
-- Employees table:        EmployeeUNI table:
-- +----+----------+       +----+-----------+          +-----------+----------+
-- | id | name     |       | id | unique_id |          | unique_id | name     |
-- +----+----------+       +----+-----------+          +-----------+----------+
-- | 1  | Alice    |       | 3  | 1         |          | null      | Alice    |
-- | 7  | Bob      |       | 11 | 2         |          | null      | Bob      |
-- | 11 | Meir     |       | 90 | 3         |          | 2         | Meir     |
-- | 90 | Winston  |       +----+-----------+          | 3         | Winston  |
-- | 3  | Jonathan |                                   | 1         | Jonathan |
-- +----+----------+                                   +-----------+----------+

-- Explanation:
-- Alice and Bob do not have a unique ID, We will show null instead.
-- The unique ID of Meir is 2.
-- The unique ID of Winston is 3.
-- The unique ID of Jonathan is 1.


SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
