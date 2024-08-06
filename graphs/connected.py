def connected_components_count(graph):
    visited = set()
    count = 0 
    for node in graph:
      if explore(graph, node, visited):
        count += 1
    return count
        
def explore(graph, node, visited): 
    if node in visited:
        return False
    visited.add(node)
    
    for neighbor in graph[node]:
      explore(graph, neighbor, visited)
    return True

connected_components_count({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) # -> 3
