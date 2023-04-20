-- https://leetcode.com/problems/tree-node/

-- Each node in the tree can be one of three types:
--    "Leaf": if the node is a leaf node.
--    "Root": if the node is the root of the tree.
--    "Inner": If the node is neither a leaf node nor a root node.
-- Write an SQL query to report the type of each node in the tree.
-- Return the result table in any order.

-- Example:
-- Input:                  Output:
-- Tree table:
-- +----+------+           +----+-------+
-- | id | p_id |           | id | type  |
-- +----+------+           +----+-------+
-- | 1  | null |           | 1  | Root  |
-- | 2  | 1    |           | 2  | Inner |
-- | 3  | 1    |           | 3  | Leaf  |
-- | 4  | 2    |           | 4  | Leaf  |
-- | 5  | 2    |           | 5  | Leaf  |
-- +----+------+           +----+-------+
-- Explanation:
-- Node 1 is the root node because its parent node is null and it has child nodes 2 and 3.
-- Node 2 is an inner node because it has parent node 1 and child node 4 and 5.
-- Nodes 3, 4, and 5 are leaf nodes because they have parent nodes and they do not have child nodes.


SELECT id,
CASE WHEN p_id IS NULL THEN 'Root'
     WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
     ELSE 'Leaf'
END AS type
FROM Tree;
