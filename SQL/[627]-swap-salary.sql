-- https://leetcode.com/problems/swap-salary/

--Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa)
--with a single update statement and no intermediate temporary tables.
--Note that you must write a single update statement, do not write any select statement for this problem.

--Example:
--Input:                                Output:
--Salary table:
--+----+------+-----+--------+          +----+------+-----+--------+
--| id | name | sex | salary |          | id | name | sex | salary |
--+----+------+-----+--------+          +----+------+-----+--------+
--| 1  | A    | m   | 2500   |          | 1  | A    | f   | 2500   |
--| 2  | B    | f   | 1500   |          | 2  | B    | m   | 1500   |
--| 3  | C    | m   | 5500   |          | 3  | C    | f   | 5500   |
--| 4  | D    | f   | 500    |          | 4  | D    | m   | 500    |
--+----+------+-----+--------+          +----+------+-----+--------+


UPDATE Salary SET sex = IF(sex = 'm', 'f', 'm');
