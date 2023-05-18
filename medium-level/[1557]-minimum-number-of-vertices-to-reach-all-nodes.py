# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where
# edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.
# Find the smallest set of vertices from which all nodes in the graph are reachable.
# It's guaranteed that a unique solution exists.
# Notice that you can return the vertices in any order.

# Example 1:
# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex.
# From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

# Example 2:
# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]
# Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them.
# Also any of these vertices can reach nodes 1 and 4.

# --------------- Runtime 1173 ms, beats 61.63%. Memory 54.7MB, beats 26.66% ---------------
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = {i: 0 for i in range(n)}

        for edge in edges:
            vertices[edge[1]] = 1

        return [key for key, val in vertices.items() if val == 0]


# Alternative solution
# --------------- Runtime 1173 ms, beats 61.63%. Memory 55.1MB, beats 14.6% ---------------

class Solution2:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = [edge[0] for edge in edges]
        reachable = [edge[1] for edge in edges]

        return list(set(vertices) - set(reachable))
