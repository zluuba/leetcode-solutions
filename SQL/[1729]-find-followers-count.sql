-- https://leetcode.com/problems/find-followers-count/

-- Write an SQL query that will, for each user, return the number of followers.
-- Return the result table ordered by user_id in ascending order.

-- Example:
-- Input:                                  Output:
-- Followers table:
-- +---------+-------------+               +---------+----------------+
-- | user_id | follower_id |               | user_id | followers_count|
-- +---------+-------------+               +---------+----------------+
-- | 0       | 1           |               | 0       | 1              |
-- | 1       | 0           |               | 1       | 1              |
-- | 2       | 0           |               | 2       | 2              |
-- | 2       | 1           |               +---------+----------------+
-- +---------+-------------+

-- Explanation:
-- The followers of 0 are {1}
-- The followers of 1 are {0}
-- The followers of 2 are {0,1}


SELECT DISTINCT user_id, count(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
