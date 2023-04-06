-- Write a SQL query for a report that provides the pairs (actor_id, director_id)
-- where the actor has cooperated with the director at least three times.
-- Return the result table in any order.

-- Example:
-- Input:                                              Output:
-- ActorDirector table:
-- +-------------+-------------+-------------+         +-------------+-------------+
-- | actor_id    | director_id | timestamp   |         | actor_id    | director_id |
-- +-------------+-------------+-------------+         +-------------+-------------+
-- | 1           | 1           | 0           |         | 1           | 1           |
-- | 1           | 1           | 1           |         +-------------+-------------+
-- | 1           | 1           | 2           |
-- | 1           | 2           | 3           |
-- | 1           | 2           | 4           |
-- | 2           | 1           | 5           |
-- | 2           | 1           | 6           |
-- +-------------+-------------+-------------+
-- Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.


SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) > 2;
