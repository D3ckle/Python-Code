# A class for nodes in a tree
class TreeNode:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    # Add a child to a tree node
    def add_child(self, data):
        new_child = TreeNode(self, data)
        self.children.append(new_child)
        return new_child
 
    # A generator function is a convenient way to create an iterator:
    # Define an iterator traversing the tree preorder
    def preorder(self):
        # 1: The node itself
        yield self
        # 2: The children
        for child in self.children:
            # Use the generator as an iterator
            for node in child.preorder():
                yield node
    def postorder(self):
        # 1: The children
        for child in self.children:
            for node in child.postorder():
                yield node
        # 2: The node itself
        yield self
    
        
if __name__ == "__main__":
    root = TreeNode('r', 'root')

    x1= root.add_child('x1')
    x2 = root.add_child('x2')

    y1 = x1.add_child('y1')

    y11 = y1.add_child('y11')
    y12 = y1.add_child('y12')

    print("post-order")
    for g in root.postorder():
        print(g.data)
    
    print("pre-order")
    for g in root.preorder():
        print(g.data)
