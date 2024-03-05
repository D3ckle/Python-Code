from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """Return True if two trees share the same key:value pairs and shape"""
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.
        if other is None: #we konw that there isnt a tree so nothing != something
            return False
        else:
            return self.root == other.root


    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self`).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        """generates a BST from a list of pre-ordered k, v tuples"""
        '''
                3:'3'
                /
            1:'1'
            / |
        0:'0' 2:'2'
        Traversals of this tree yields the following lists of k:v tuples:
        pre-order: [(3,'3'), (1,'1'), (0,'0'), (2,'2')]'''
        #root then left then right

        #since the list itself is in preorder, i dont need to worry about switching aorund nodes, etc., only put them in the list
        
        temp = BSTMap()
        for i in L: #i = a tuple with key:value pairs
            temp.put(i[0], i[1]) #should be able to call the put method and let it handle adding, no issues
        return temp
        
        

    @staticmethod
    def frompostorder(L):
        """generates a BST from a list of pre-ordered k, v tuples"""
        '''
                3:'3'
                /
            1:'1'
            / |
        0:'0' 2:'2'
        Traversals of this tree yields the following lists of k:v tuples:
        post-order: [(0,'0'), (2,'2'), (1,'1'), (3,'3')]'''
        #build from left to right to root
        temp = MyBSTMap()
        for i in range(len(L)-1, -1, -1): #reading the list backwards - avoid reverse() method
            temp.put(L[i][0], L[i][1]) #should be able to call the put method and let that handle adding, no issues
        return temp
            


#===============================================================================================================================
#===============================================================================================================================
#===============================================================================================================================


class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    '''
    def __init__(self, key, value = None):
    """Create a new BSTNode"""
    self.key = key
    self.value = value
    self.left = None
    self.right = None
    '''

    # TODO: implement the method below
    def __eq__(self, other):
        """compares 2 BSTNodes and see if theyre the same"""
        if other is None:
            return False
        #1) They have the same key:value pairs
        if self.key == other.key and self.value == other.value:
        #2) The subtrees rooted at their left and right children are equal
            if self.left == other.left and self.right == other.right: #----------recursive call?
                return True #the nodes are equal
        return False #did not pass the if statements, Nodes are not equal
