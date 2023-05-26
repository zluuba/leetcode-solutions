-- https://leetcode.com/problems/invalid-tweets/

-- Write an SQL query to find the IDs of the invalid tweets.
-- The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
-- Return the result table in any order.

-- Example:
-- Input:                                                  Output:
-- Tweets table:
-- +----------+----------------------------------+         +----------+
-- | tweet_id | content                          |         | tweet_id |
-- +----------+----------------------------------+         +----------+
-- | 1        | Vote for Biden                   |         | 2        |
-- | 2        | Let us make America great again! |         +----------+
-- +----------+----------------------------------+

-- Explanation:
-- Tweet 1 has length = 14. It is a valid tweet.
-- Tweet 2 has length = 32. It is an invalid tweet.


SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
