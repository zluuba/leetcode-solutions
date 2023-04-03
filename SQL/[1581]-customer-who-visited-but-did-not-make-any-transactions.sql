--Write a SQL query to find the IDs of the users who visited without making any transactions and the number
--of times they made these types of visits.
--Return the result table sorted in any order.
--The query result format is in the following example.

--Example:
--Input:
--Visits                              Transactions
--+----------+-------------+          +----------------+----------+--------+
--| visit_id | customer_id |          | transaction_id | visit_id | amount |
--+----------+-------------+          +----------------+----------+--------+
--| 1        | 23          |          | 2              | 5        | 310    |
--| 2        | 9           |          | 3              | 5        | 300    |
--| 4        | 30          |          | 9              | 5        | 200    |
--| 5        | 54          |          | 12             | 1        | 910    |
--| 6        | 96          |          | 13             | 2        | 970    |
--| 7        | 54          |          +----------------+----------+--------+
--| 8        | 54          |
--+----------+-------------+

--Output:
--+-------------+----------------+
--| customer_id | count_no_trans |
--+-------------+----------------+
--| 54          | 2              |
--| 30          | 1              |
--| 96          | 1              |
--+-------------+----------------+


SELECT customer_id, count(Visits.customer_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Transactions.visit_id = Visits.visit_id
WHERE Transactions.amount IS NULL
GROUP BY Visits.customer_id
ORDER BY count_no_trans DESC;
