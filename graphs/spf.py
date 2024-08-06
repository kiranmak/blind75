from collections import deque

# BFS will be right approach than DFS
def shortest_path(edges, node_A, node_B):

    graph = buildGraph(edges)
    visited = set((node_A))

    dq = deque((node_A, 0))
    while dq:
        node, dist = dq.popleft()
        if node == node_B: return dist
        
        for neighbor in graph:
            if neighbor not in visited:
                dq.append((neighbor, dist + 1))
                visited.add(neighbor)
                
    return -1
        
def buildGraph(edges):
  graf = {}
  for edge in edges:
    f, s = edge[0], edge[1]
    if  f not in graf: graf[f] = []
    if  s not in graf: graf[s] = []
    graf[f].append(s)
    graf[s].append(f)

  return graf
  
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

shortest_path(edges, 'w', 'z') # -> 2