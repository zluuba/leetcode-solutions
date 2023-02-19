-- Table: Employee

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.


-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.
-- The query result format is in the following example.


SELECT emp.name as Employee
FROM Employee AS mngr
INNER JOIN Employee AS emp ON mngr.id = emp.managerID
WHERE emp.salary > mngr.salary;
