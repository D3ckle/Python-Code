# A class for nodes in a tree
class TreeNode:
    def __init__(self, parent, level, data):
        self.parent = parent
        self.level = level
        self.data = data
        self.children = []

    # Add a child to a tree node
    def add_child(self, data):
        new_child = TreeNode(self, self.level + 1, data)
        self.children.append(new_child)
        return new_child

    # Return a list of the ancestors of a node
    def get_ancestors(self):
        if self.parent:
            return [self] + self.parent.get_ancestors()
        else:
            return [self]

    # Return a list of the leaves
    def get_leaves(self):
        # If the node is a leaf
        if not self.children:
            # Return the node itself
            return [self]

        leaves = []
        # Proceed recursively
        for child in self.children:
            leaves = leaves + child.get_leaves()

        return leaves

    # Return a list of the edges
    def get_edges(self):
        # If the node is a leaf
        if not self.children:
            # Return the node itself
            return []

        edges = []
        # Proceed recursively
        for child in self.children:
            edges = edges + [(self, child)] + child.get_edges()

        return edges


    # A generator function is a convenient way to create an iterator:
    # Define an iterator traversing the tree preorder
    def preorder(self):
        # 1: The node itself
        yield self

        # 2: The children
        for child in self.children:
            # Use the generator as an iterator
            yield from child.preorder()
            # The 'yield from' can also be written:
            # for node in child.preorder():
            #     yield node

    # Define an iterator traversing the tree postorder
    def postorder(self):
        # 1: The children
        for child in self.children:
            # Use the generator as an iterator
            yield from child.postorder()
            # The 'yield from' can also be written:
            # for node in child.postorder():
            #     yield node

        # 2: The node itself
        yield self


class Tree:
    def __init__(self, data):
        self.root = TreeNode(None, 0, data)
        self.nb_nodes = 1
        self.depth = 1
        

    def __len__(self):
        return self.nb_nodes

    def add_child(self, node, data):
        #print(data)
        #print(node)
        child = node.add_child(data)
        if self.depth < child.level:
            self.depth = child.level
        #self.compute_relative_positions()
        return child


    def get_edges(self):
        return self.root.get_edges()

    def get_width(self):
        return len(self.root.get_leaves())

    def get_depth(self):
        return self.depth

if __name__ == '__main__':
 
    #n = 7
    #bst = Tree('m')
    
    tree = Tree('r')
    x1 = tree.add_child(tree.root,'x1')
    x2 = tree.add_child(tree.root,'x2')
    y1 = tree.add_child(x1,'y1')
    y11 = tree.add_child(y1,'y11')
    y12 = tree.add_child(y1,'y12')
    print('Tree Depth: ',tree.get_depth())

    gen = tree.root.postorder()
    for g in gen:
        print(g.data)

    edges = tree.root.get_edges()
    for eg in edges:
        print(eg[0].data +'====>'+ eg[1].data)
    print(len(tree))
