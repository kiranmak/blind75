import sys
def largest_component(graph):
    visited = set()
    count = 0
    for node in graph:
      node_count = explore(graph, node, visited)
      if count < node_count:
        count = node_count
    return count
        
def explore(graph, node, visited): 
  if node in visited: return 0
    
  visited.add(node)
  node_count = 1
    
  for neighbor in graph[node]:
    node_count += explore(graph, neighbor, visited)
  return node_count

  
largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4
