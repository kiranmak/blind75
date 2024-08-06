def undirected_path(edges, node_A, node_B):
  graph = buildGraph(edges)
  visited = set()
  return hasPath(graph, node_A, node_B, visited)
  pass # todo

def hasPath(graph, A,B, visited):
  if A in visited: return False
  if A == B: return True

  visited.add(A)
  
  for neighbor in graph[A]:
    if hasPath(graph, neighbor, B, visited):
      return True
  return False
  
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
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'm', 'j') # -> True
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'k', 'o') # -> False