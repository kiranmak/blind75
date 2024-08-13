'''
261. Graph Valid Tree
Description
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.


'''
from collections import defaultdict, deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        visited = set()
        graph = self.buildGraph(n, edges)
        if not self.dfs(0,-1, graph, visited):
            return False

        return True if len(visited) == n else False

    def dfs(self, node, parent, graph, visited):

        if node in visited:
            return False #cycle traversed

        visited.add(node)
        for nbr in graph[node]:
            if nbr == parent:
                continue
            if not self.dfs(nbr, node, graph, visited):
                return False

        return True
            
    def buildGraph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = [] 

        for f,s in edges:
            graph[f].append(s)
            graph[s].append(f) # undirected graph
        #for n in graph:
        #    print(n, "->", graph[n])
        return graph
         
    
s = Solution()

edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
ans = s.validTree(n = 5, edges = edges)
print("for tree:", edges, "ans", ans)
edges = [[0,1],[0,2],[0,3],[1,4]]
ans = s.validTree(n = 5, edges = edges)
print("for tree:", edges, "ans", ans)
edges = [[0,1],[2,1],[3,2],[3,1],[4,1]]
ans = s.validTree(n = 5, edges=edges)
print("for tree:", edges, "ans", ans)
edges = [[0,1],[2,0],[3,0],[1,4]]
ans = s.validTree(n = 5, edges=edges)
print("for tree:", edges, "ans", ans)
            
    