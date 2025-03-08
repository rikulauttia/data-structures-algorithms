def find_components(nodes, edges):
    graph = {node: [] for node in nodes}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for node in nodes:
        if node not in visited:
            component = []
            dfs(node, component)
            component.sort()
            components.append(component)

    components.sort()
    
    return components

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]