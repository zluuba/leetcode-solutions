-- Write an SQL query to find the ids of products that are both low fat and recyclable.

-- Return the result table in any order.

-- The query result format is in the following example.

--------------- Runtime 1104 ms, beats 21.12% ---------------


SELECT product_id FROM Products
WHERE low_fats='Y' AND recyclable='Y';
