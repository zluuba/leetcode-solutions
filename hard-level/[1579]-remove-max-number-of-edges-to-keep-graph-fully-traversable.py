# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

# Alice and Bob have an undirected graph of n nodes and three types of edges:
# - Type 1: Can be traversed by Alice only.
# - Type 2: Can be traversed by Bob only.
# - Type 3: Can be traversed by both Alice and Bob.

# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between
# nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges,
# the graph can still be fully traversed by both Alice and Bob.
# The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob.
# Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

# Example 2:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

# Example 3:
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes.
# Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

# --------------- Runtime 2368 ms, beats 15.10%. Memory 56.7MB, beats 18.24% ---------------
from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p1, p2 = self.find(p), self.find(q)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            p1, p2 = p2, p1

        self.n -= 1
        self.parent[p1] = p2
        self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)

        cnt = 0
        edges.sort(reverse=True)

        for t, src, dst in edges:
            src, dst = src - 1, dst - 1
            if t == 3:
                cnt += not (alice.union(src, dst) and bob.union(src, dst))
            elif t == 2:
                cnt += not bob.union(src, dst)
            else:
                cnt += not alice.union(src, dst)

        if alice.n == bob.n == 1:
            return cnt
        return -1
