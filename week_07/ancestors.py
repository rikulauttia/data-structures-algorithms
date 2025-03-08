class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def ancestor(node, a, b):
    if node.value == a:
        return is_descendant(node, b)
    
    for child in node.children:
        if ancestor(child, a, b):
            return True
            
    return False
    
def is_descendant(node, value):
    if node.value == value:
        return True
        
    for child in node.children:
        if is_descendant(child, value):
            return True
            
    return False

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False