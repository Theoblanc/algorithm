
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


# def dfs(graph, node):
#     visit = []
#     stack = []

#     stack.append(node)
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             stack.extend(graph[node])

#     return visit


def dfs(graph, start_node):
    visited = []
    stack = []

    stack.append(start_node)
    while start_node:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited
    
