-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

-- Write an SQL query to report the number of unique subjects each teacher teaches in the university.
-- Return the result table in any order.

-- Example:
-- Input:                                          Output:
-- Teacher table:
-- +------------+------------+---------+           +------------+-----+
-- | teacher_id | subject_id | dept_id |           | teacher_id | cnt |
-- +------------+------------+---------+           +------------+-----+
-- | 1          | 2          | 3       |           | 1          | 2   |
-- | 1          | 2          | 4       |           | 2          | 4   |
-- | 1          | 3          | 3       |           +------------+-----+
-- | 2          | 1          | 1       |
-- | 2          | 2          | 1       |
-- | 2          | 3          | 1       |
-- | 2          | 4          | 1       |
-- +------------+------------+---------+

-- Explanation:
-- Teacher 1:
--   - They teach subject 2 in departments 3 and 4.
--   - They teach subject 3 in department 3.
-- Teacher 2:
--   - They teach subject 1 in department 1.
--   - They teach subject 2 in department 1.
--   - They teach subject 3 in department 1.
--   - They teach subject 4 in department 1.


SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
