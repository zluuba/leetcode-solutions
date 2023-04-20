-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

-- Write an SQL query to find the employees who earn more than their managers.
-- Return the result table in any order.

-- Example:
-- Input:                                      Output:
-- Employee table:
-- +----+-------+--------+-----------+         +----------+
-- | id | name  | salary | managerId |         | Employee |
-- +----+-------+--------+-----------+         +----------+
-- | 1  | Joe   | 70000  | 3         |         | Joe      |
-- | 2  | Henry | 80000  | 4         |         +----------+
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+
-- Explanation: Joe is the only employee who earns more than his manager.


SELECT emp.name as Employee
FROM Employee AS mngr
INNER JOIN Employee AS emp ON mngr.id = emp.managerID
WHERE emp.salary > mngr.salary;
