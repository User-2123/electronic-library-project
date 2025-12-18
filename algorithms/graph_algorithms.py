from collections import deque

def bfs(graph, start_node):
    """
    Обход в ширину.
    graph: словарь {node: [neighbors]}
    """
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

def dfs(graph, start_node, visited=None):
    """
    Обход в глубину (рекурсивный).
    """
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    result = [start_node]

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result