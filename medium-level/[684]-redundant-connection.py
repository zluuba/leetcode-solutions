# https://leetcode.com/problems/redundant-connection/

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge
# between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

# Example 1:
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Example 2:
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

# --------------- Runtime 61 ms, beats 84.66%. Memory 15.2MB, beats 41.36% ---------------
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.size = {}
        for i in range(n):
            self.par[i] = i
            self.size[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.size[p1] > self.size[p2]:
            self.par[p2] = p1
            self.size[p2] += self.size[p1]
        else:
            self.par[p1] = p2
            self.size[p1] += self.size[p2]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)

        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return [n1, n2]
