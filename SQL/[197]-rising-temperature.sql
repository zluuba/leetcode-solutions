-- https://leetcode.com/problems/rising-temperature/

-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.

-- Input:                                  Output:
-- Weather table:
-- +----+------------+-------------+       +----+
-- | id | recordDate | temperature |       | id |
-- +----+------------+-------------+       +----+
-- | 1  | 2015-01-01 | 10          |       | 2  |
-- | 2  | 2015-01-02 | 25          |       | 4  |
-- | 3  | 2015-01-03 | 20          |       +----+
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Explanation:
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).


SELECT w1.id AS Id
FROM Weather AS w1, Weather AS w2
WHERE
    DATEDIFF(w1.recordDate, w2.recordDate) = 1
    AND w1.temperature > w2.temperature;
