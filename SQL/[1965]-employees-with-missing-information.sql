-- https://leetcode.com/problems/employees-with-missing-information/

-- Write an SQL query to report the IDs of all the employees with missing information.
-- The information of an employee is missing if:
-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.

-- Input:                                                        Output:
-- Employees table:                Salaries table:
-- +-------------+----------+      +-------------+--------+      +-------------+
-- | employee_id | name     |      | employee_id | salary |      | employee_id |
-- +-------------+----------+      +-------------+--------+      +-------------+
-- | 2           | Crew     |      | 5           | 76071  |      | 1           |
-- | 4           | Haven    |      | 1           | 22517  |      | 2           |
-- | 5           | Kristian |      | 4           | 63539  |      +-------------+
-- +-------------+----------+      +-------------+--------+
-- Explanation:
-- Employees 1, 2, 4, and 5 are working at this company.
-- The name of employee 1 is missing.
-- The salary of employee 2 is missing.


SELECT employees.employee_id FROM employees
LEFT JOIN salaries ON employees.employee_id = salaries.employee_id
WHERE salaries.salary IS NULL

UNION

SELECT salaries.employee_id FROM salaries
LEFT JOIN employees ON employees.employee_id = salaries.employee_id
WHERE employees.name IS NULL

ORDER BY employee_id;
