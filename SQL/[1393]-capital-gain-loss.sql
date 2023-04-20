-- https://leetcode.com/problems/capital-gainloss/

-- Write an SQL query to report the Capital gain/loss for each stock.
-- The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
-- Return the result table in any order.

-- Input:                                                      Output:
-- Stocks table:
-- +---------------+-----------+---------------+--------+      +---------------+-------------------+
-- | stock_name    | operation | operation_day | price  |      | stock_name    | capital_gain_loss |
-- +---------------+-----------+---------------+--------+      +---------------+-------------------+
-- | Leetcode      | Buy       | 1             | 1000   |      | Corona Masks  | 9500              |
-- | Corona Masks  | Buy       | 2             | 10     |      | Leetcode      | 8000              |
-- | Leetcode      | Sell      | 5             | 9000   |      | Handbags      | -23000            |
-- | Handbags      | Buy       | 17            | 30000  |      +---------------+-------------------+
-- | Corona Masks  | Sell      | 3             | 1010   |
-- | Corona Masks  | Buy       | 4             | 1000   |
-- | Corona Masks  | Sell      | 5             | 500    |
-- | Corona Masks  | Buy       | 6             | 1000   |
-- | Handbags      | Sell      | 29            | 7000   |
-- | Corona Masks  | Sell      | 10            | 10000  |
-- +---------------+-----------+---------------+--------+
-- Explanation:
-- Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
-- Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
-- Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$
-- and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$.
-- Capital gain/loss is the sum of capital gains/losses for each ('Buy' -> 'Sell')
-- operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.


SELECT
  stock_name,
  SUM(
      CASE WHEN operation = 'Sell' THEN price ELSE -price END
  ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
