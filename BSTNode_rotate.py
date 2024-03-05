from math import floor, ceil, log2
import math
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None   # left child
        self.right = None  # right child
        self.weight = 1    # number of nodes in subtree rooted at this node
    
    def put(self, key, value, parent=None):
        if self.key == key:
            self.value = value
        
        elif self.key > key: # search left
            if self.left: self.left.put(key, value, parent=self)
            else: self.left = BSTNode(key, value)

        elif self.key < key: # search right
            if self.right: self.right.put(key, value, parent=self)
            else: self.right = BSTNode(key, value)

        # update weights to keep track of any new nodes
        left_w, right_w = self.update_weight()

        # rotate if 1 child is 3x heavier than the other
        if (max(left_w, right_w) + 1) / (min(left_w, right_w) + 1) >= 3:
            if left_w > right_w: return self.rotate_right(parent)
            else: return self.rotate_left(parent)
        return self

 
    def update_weight(self):
        left_w = self.left.weight if self.left else 0
        right_w = self.right.weight if self.right else 0
        self.weight = left_w + right_w + 1

        return left_w, right_w

        

    def get(self, key):
        # 3 cases:
        #    1) self.key == key: return self
        #    2) self.key > key: search left subtree
        #    3) self.key < key: search right subtree

        if self.key == key: return self
    
        if self.key > key:
            if self.left: return self.left.get(key)

        if self.key < key:
            if self.right: return self.right.get(key)

        raise KeyError("key {} is not in tree".format(key))

    def rotate_left(self, parent):
        #       z                      z
        #      /                      / 
        #     /                      /
        #    x         ===>         y
        #   / \                    / \
        #  /   \                  /   \
        # a     y                x     g
        #      / \              / \
        #     /   \            /   \
        #    b     g          a     b
        # Pseudo code:
        #    new = old.right
        #    old.right = new.left
        #    new.left = old
        #    parent.child = new
        old, new = self, self.right
        old.right = new.left
        new.left = old

        old.update_weight()
        new.update_weight()

        if parent:
            left_child = self.key < parent.key
            if left_child: parent.left = new
            else: parent.right = new
        
        return new

    def rotate_right(self, parent):
        old, new = self, self.left
        old.left = new.right
        new.right = old

        old.update_weight()
        new.update_weight()

        if parent:
            left_child = self.key < parent.key
            if left_child: parent.left = new
            else: parent.right = new
        
        return new
        
        # This is similar to rotate_left. Try to code it!
    
    def print_subtree(self):
        # lines is a list of lists: each sublist contains
        # a string corresponding to a line to be printed
        lines = self._print_subtree(lines=None)

        # use the string "join" method to join all objects in
        # an iterable with a separator.
        return "\n".join(lines)
    
    def _print_subtree(self, current_depth = None, lines = None,  max_depth = None, w=None):
        # initialize variables the first time this is called
        if lines is None:
            height = math.floor(math.log2(self.weight))  + 2    # height to draw. Increasing this will let you draw more unbalanced trees.
            n_bottom = 2**height
            n_levels = height + 1                               # levels in tree
            n_lines = 3*n_levels                                # lines to print tree
            w = 2*n_bottom + 2*n_bottom/2 + 2*(n_bottom/2 - 1)  # calculate width of bottom level
            w = 2**math.ceil(math.log2(w))                      # round w to a power of 2
            
            lines = ["" for i in range(n_lines)]                # lines to print

            max_depth = height-1                                 
            current_depth = 0                                   # initialize current_depth
       
        n_items = 2**(current_depth) # number of items possible on this level
        item_width = w // n_items    # width of an item's string at this level

        # append current node to this line
        if self.left and self.right:
            lines[current_depth*3] += "{:02}".format(self.key).center(item_width//2-2, "_").center(item_width)
        elif self.left:
            line = "  " + "_"*(item_width//4-2) + "{:02}".format(self.key) + " "*(item_width//4)
            lines[current_depth*3] += line.center(item_width)
        elif self.right:
            line = " "*(item_width//4) + "{:02}".format(self.key) + "_"*(item_width//4 - 2) + "  "
            lines[current_depth*3] += line.center(item_width)
        else:
            lines[current_depth*3] += "{:02}".format(self.key).center(item_width)
        
        # recursively call on left and right children
        if self.left:
            lines[current_depth*3 + 1] += " /".center(item_width//2) 
            lines[current_depth*3 + 2] += "/ ".center(item_width//2)
            self.left._print_subtree(current_depth+1, lines, max_depth, w)
        else:
            # append blank lines for all possible left children
            for i in range(current_depth, max_depth+1):
                for j in range(1,4):
                    lines[i*3+j] += "".center(item_width//2)
            
        if self.right:
            lines[current_depth*3 + 1] += "\\ ".center(item_width//2)
            lines[current_depth*3 + 2] += " \\".center(item_width//2)
            self.right._print_subtree(current_depth+1, lines, max_depth, w)
        else:
            # append blank lines for all possible right children
            for i in range(current_depth, max_depth+1): 
                for j in range(1,4):
                    lines[i*3+j] += "".center(item_width//2)

        return lines  