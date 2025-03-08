def connected(nodes, edges):
    if not nodes:
        return True
    
    if not edges:
        return len(nodes) <= 1
    
    graph = {node: [] for node in nodes}
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    visited = set()
    queue = [nodes[0]]

    while queue:
        node = queue.pop(0)
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return len(visited) == len(nodes)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True