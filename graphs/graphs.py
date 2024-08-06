from collections import deque

def depthFirstSearchPrint(graph, source):
    stack = [source]
    while len(stack) > 0:
        node = stack.pop()
        print(node)
        for neighbor in graph[node]:
           stack.append(neighbor) 
    
def depthFirstSearchPrintRec(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstSearchPrintRec(graph, neighbor)

def breadthFirstSearchPrint(graph, source):
    dq = deque([source])
    print("breadthFirstSearchPrint")
    while dq:
        node = dq.popleft()
        print(node)
        for neighbor in graph[node]:
            dq.append(neighbor)
        
def buildGraph(edges):
  graf = {}
  for edge in edges:
    f, s = edge[0], edge[1]
    if  f not in graf: graf[f] = []
    if  s not in graf: graf[s] = []
    graf[f].append(s)
    graf[s].append(f)

  return graf

graph = {
    'a': ['b', 'c'], 
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':[],
    'f':[]
    }

depthFirstSearchPrint(graph, 'a')
print("recursion")
depthFirstSearchPrintRec(graph, 'a')
breadthFirstSearchPrint(graph, 'a')
print("breadthFirstSearchPrintRec")