'''
class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
'''

from collections import deque
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def makeGraph(self, adjList):
        nmap = {}
        for i, adj in enumerate(adjList):
            n = self.getNode(nmap, i+1)
            for j in adj:
                adj_n = self.getNode(nmap, j)
                n.neighbors.append(adj_n)
        return nmap[1]

    def show(self, node):
        dq = deque([node])
        visited = set([node.val])
        adjList = []
        while dq:
            n = dq.popleft() 
            #print("traversing node ", n.val)
            nlist = []
            for neighbor in n.neighbors:
                nlist.append(neighbor.val)
                if neighbor.val not in visited:
                    dq.append(neighbor)
                    visited.add(neighbor.val)
            if nlist:
                adjList.append(nlist)
        print(adjList)
                
    def getNode(self, nmap, val):
        if val not in nmap:
            nmap[val] = Node(val, neighbors=None)
        return nmap[val]

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if  node is None:
            return None

        dq = deque([node])
        visited = set([node.val])
        created = {}  # node cloned already
        while dq:
            n = dq.popleft()
            clone = self.getNode(created, n.val)
            for neighbor in n.neighbors:
                clone_neig = self.getNode(created, neighbor.val)
                clone.neighbors.append(clone_neig)

                if neighbor.val not in visited:
                    dq.append(neighbor)
                    visited.add(neighbor.val)

        return created[1]
        
    
s = Solution()
adjList = [[2,4],[1,3],[2,4],[1,3]]
first = s.makeGraph(adjList)
clone = s.cloneGraph(first)
s.show(clone)
