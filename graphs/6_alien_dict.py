'''
269. Alien Dictionary
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "y"
  "z"
]

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''
from collections import Counter, defaultdict, deque
from typing import List

# approach:
# topological sort: 
# 1. first letter of each word in lexical order.
# 2. if prev letter is same than next letters of those words are in lexical order.
# 3. create edges between lexical order and subsequently graph.
# 4. from graph, start with first letter.
# 4.1. chase its neighbor 
# 5. there could be some with no order known - empty adjacency.
# 6 look for cycle by visited logic.


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        alphabets = {}
        for word in words:
            for c in word:
                alphabets[c] = 0
        
        graph = self.makeGraph(words, alphabets)
        order = self.topoSort(graph, alphabets)
        #return order
        return "".join(order) if order else ""
    
    def makeGraph(self, words, in_degree):
        graph = defaultdict(set)
        for i in range(1,len(words)):
            prev = words[i - 1]
            curr = words[i]
            
            for p, c in zip(prev, curr):
                if p != c:
                    if p not in graph:
                        graph[p] = set()
                    graph[p].add(c)
                    in_degree[c] += 1
                    break  # cant guarantee rest of the order
        
        for item in graph.keys():
            print(item, "-->", graph[item])
        for item in in_degree.keys():
            print(item, "= indegree", in_degree[item])
       
        return graph

    def topoSort(self, graph, alphabets):
        
        dfs = []
        # make queue from indegree= 0 (starts)
        order = deque([])
        for c in alphabets:
            if alphabets[c] == 0:
                order.appendleft(c)

        while order:
            x = order.popleft()
            dfs.append(x)
            for neighbor in graph[x]:
                alphabets[neighbor] -= 1
                if alphabets[neighbor] == 0: 
                    order.append(neighbor)
        return dfs

    def showGraph(self, graph):
        for s in graph:
            print(s, "-->", graph[s])
        print("\n")
    def alien_alphabet(self, words: List[str]) -> str:
        output = []
        # 1: Populate adjacency list and in-degree list
        adjacency_list = defaultdict(set)
        in_degree = Counter({char: 0 for word in words for char in word})
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            # Edge case: word 2 is a shorter prefix of word 1
            if len(word_1) > len(word_2) and word_1.startswith(word_2):
                return ''
            for start_char, end_char in zip(word_1, word_2):
                if start_char != end_char:
                    if end_char not in adjacency_list[start_char]:
                        adjacency_list[start_char].add(end_char)
                        in_degree[end_char] += 1
                    break
        # 2: Topological sort
        # Populate queue with zero in-degree nodes
        q = deque([char for char in in_degree if in_degree[char] == 0])
        while q:
            node = q.popleft()
            output.append(node)
            # We are removing this node, so go through its neighbors and decrement their indegrees
            for neighbor in adjacency_list[node]:
                in_degree[neighbor] -= 1
                # If at any point a vector has no indgrees left, add it to the queue
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        # Cylce detection: if we visited fewer nodes than there are vectors in our graph, there's a cycle - return an empty string
        if len(output) < len(in_degree): return ''
        return ''.join(output)
            
                
input = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
#input = [ "z", "y", "z","x"]
#input =  ["kaa", "akcd", "akca", "cak", "cad"]
input = ["zy","zx"] #Expected "yxz"
s = Solution()
#order = s.alienOrder(input)
order = s.alien_alphabet(input)
print("dict:", order)