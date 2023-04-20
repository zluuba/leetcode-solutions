-- https://leetcode.com/problems/second-highest-salary/

-- Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary,
-- the query should report null.

-- Example 1:
-- Input:                  Output:
-- Employee table:
-- +----+--------+         +---------------------+
-- | id | salary |         | SecondHighestSalary |
-- +----+--------+         +---------------------+
-- | 1  | 100    |         | 200                 |
-- | 2  | 200    |         +---------------------+
-- | 3  | 300    |
-- +----+--------+

-- Example 2:
-- Input:                      Output:
-- Employee table:
-- +----+--------+             +---------------------+
-- | id | salary |             | SecondHighestSalary |
-- +----+--------+             +---------------------+
-- | 1  | 100    |             | null                |
-- +----+--------+             +---------------------+


SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
