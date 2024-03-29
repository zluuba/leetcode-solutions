-- https://leetcode.com/problems/calculate-special-bonus/

-- Write an SQL query to calculate the bonus of each employee.
-- The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and
-- the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
-- Return the result table ordered by employee_id.

-- Example:
-- Input:                                      Output:
-- Employees table:
-- +-------------+---------+--------+          +-------------+-------+
-- | employee_id | name    | salary |          | employee_id | bonus |
-- +-------------+---------+--------+          +-------------+-------+
-- | 2           | Meir    | 3000   |          | 2           | 0     |
-- | 3           | Michael | 3800   |          | 3           | 0     |
-- | 7           | Addilyn | 7400   |          | 7           | 7400  |
-- | 8           | Juan    | 6100   |          | 8           | 0     |
-- | 9           | Kannon  | 7700   |          | 9           | 7700  |
-- +-------------+---------+--------+          +-------------+-------|
-- Explanation:
-- The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
-- The employee with ID 3 gets 0 bonus because their name starts with 'M'.
-- The rest of the employees get a 100% bonus.


SELECT employee_id,
       IF(employee_id % 2 = 1 AND name NOT LIKE 'M%', salary, 0) AS bonus
FROM employees
ORDER BY employee_id;


-- Alternative solution:

SELECT employee_id,
CASE
    WHEN (name not LIKE 'M%' AND employee_id % 2 != 0)
    THEN salary ELSE 0
END AS bonus
FROM Employees
ORDER BY employee_id;
