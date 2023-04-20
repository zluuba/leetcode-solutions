-- https://leetcode.com/problems/top-travellers/

-- Write an SQL query to report the distance traveled by each user.
-- Return the result table ordered by travelled_distance in descending order,
-- if two or more users traveled the same distance, order them by their name in ascending order.

-- Example:
-- Input:                                                            Output:
-- Users table:                Rides table:
-- +------+-----------+        +------+----------+----------+        +----------+--------------------+
-- | id   | name      |        | id   | user_id  | distance |        | name     | travelled_distance |
-- +------+-----------+        +------+----------+----------+        +----------+--------------------+
-- | 1    | Alice     |        | 1    | 1        | 120      |        | Elvis    | 450                |
-- | 2    | Bob       |        | 2    | 2        | 317      |        | Lee      | 450                |
-- | 3    | Alex      |        | 3    | 3        | 222      |        | Bob      | 317                |
-- | 4    | Donald    |        | 4    | 7        | 100      |        | Jonathan | 312                |
-- | 7    | Lee       |        | 5    | 13       | 312      |        | Alex     | 222                |
-- | 13   | Jonathan  |        | 6    | 19       | 50       |        | Alice    | 120                |
-- | 19   | Elvis     |        | 7    | 7        | 120      |        | Donald   | 0                  |
-- +------+-----------+        | 8    | 19       | 400      |        +----------+--------------------+
--                             | 9    | 7        | 230      |
--                             +------+----------+----------+
-- Explanation:
-- Elvis and Lee traveled 450 miles, Elvis is the top traveler as his name is alphabetically smaller than Lee.
-- Bob, Jonathan, Alex, and Alice have only one ride and we just order them by the total distances of the ride.
-- Donald did not have any rides, the distance traveled by him is 0.


SELECT
  users.name,
  SUM(
    IF(Rides.distance IS NULL, 0, Rides.distance)
  ) AS travelled_distance
FROM users
LEFT JOIN Rides ON Rides.user_id = Users.id
GROUP BY users.id
ORDER BY travelled_distance DESC, users.name ASC;
