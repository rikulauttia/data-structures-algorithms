class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_children(node):
    children_counts = []
    def traverse(current_node):
        children_counts.append(len(current_node.children))
        for child in current_node.children:
            traverse(child)
    traverse(node)
    children_counts.sort()
    
    return children_counts

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_children(tree1)) # [0, 0, 0, 0, 1, 2, 3]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_children(tree2)) # [0, 1, 1, 1]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_children(tree3)) # [0, 0, 0, 3]