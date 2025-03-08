class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def find_levels(node):
    if node is None:
        return []

    result = []
    current_level = [node]
    while current_level:
        level_values = [n.value for n in current_level]
        level_values.sort()
        result.append(level_values)
        next_level = []
        for n in current_level:
            if n.children:
                next_level.extend(n.children)
        current_level = next_level
    return result

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]