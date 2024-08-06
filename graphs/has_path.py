'''
Write a function, hasPath, that takes in an object
representing the adjacency list of a directed acyclic
graph and two nodes (src, dst). 
The function should return a boolean indicating whether 
or not there exists a directed path between the 
source and destination nodes.

Hey. This is our first graph problem, 
so you should be liberal with watching the Approach and 
Walkthrough. Be productive, not stubborn. -AZ

from collections import deque
'''
def has_path_rec(graph, src, dst):
  if src == dst: return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False    

def has_path(graph, src, dst):
  if src == dst: return True
  dq = deque([src])
  while dq:
    node = dq.popleft()
    for neighbor in graph[node]:
      if neighbor == dst:
        return True
      dq.append(neighbor)
    
  return False  
    
graph = {
    'f': ['g', 'i'], 
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j':['i'],
    'k':[]
    }
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'w') # True
