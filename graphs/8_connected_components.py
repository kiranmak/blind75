'''
Count Connected Components
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
Input: n=3 edges=[[0,1], [0,2]]
Output: 1
Example 2:
Input: n=6 edges=[[0,1], [1,2], [2,3], [4,5]]
Output: 2
'''
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if edges == []:
            return n
        
        graph = self.buildGraph(n, edges)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                self.dfs(i, -1, graph, visited)
                count += 1
                print("visited=", visited)
            if len(visited) == n:
                return count
        return count

    def dfs(self, node, prev, graph, vis):
        if node in vis:
            return
        vis.add(node)
        for nbr in graph[node]:
            if nbr == prev:
                continue
            self.dfs(nbr, node, graph, vis)
            
        return
    
    def buildGraph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for f,s in edges:
            graph[f].append(s)
            graph[s].append(f)
        
        for v in graph:
            print(v, "-->", graph[v])

        return graph

s = Solution()
edges=[[0,1], [0,2]] # n=3
edges=[[0,1], [1,2], [2,3], [4,5]] #n=6
count = s.countComponents(6, edges=edges)
print("components for ", edges, "are =", count)
