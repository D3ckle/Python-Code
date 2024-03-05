import unittest, random
random.seed(652)
from MyBSTMap import MyBSTMap, BSTNode

class TestMyBSTMap(unittest.TestCase):

    '''2 empty trees (should be equal)
    2 equal trees with several levels of nodes
    2 unequal trees with several layers of nodes:
    a) same key:value pairs, different shapes
    b) same shapes, different key:value pairs'''


    def test_equal_empty(self):
        """tests if 2 empty binear search trees are equal"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        self.assertTrue(bst1 == bst2)
        print("test_equal_empty OK")


    def test_equal_multiplenodes(self):
        """tests if 2 BST are equal with multiple nodes in the BST"""

        L = []
        for i in range(8, 0, -1):
            L.append((i, str(i)))

        bst1 = MyBSTMap()
        bst2 = MyBSTMap()

        for i in L:
            bst1.put(i[0], i[1])
            bst2.put(i[0], i[1])

        #print("\n", bst1)
        #print("\n", bst2)

        self.assertTrue(bst1 == bst2)
        print("test_equal_multiplenodes OK")


    def test_notequal_multiplenodes_difshapes(self):
        """asserts that 2 BSTs are different with different tree structures, (could have the same # of nodes / same values)"""
        L = []
        for i in range(8): #k:v of i:'i' 0 through 7
            L.append((i, str(i)))
        
            
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()

        for i in range(8):
            bst1.put(L[i][0], L[i][1])

        for i in range(7, -1, -1):
            bst2.put(L[i][0], L[i][1])

        #print("\n", bst1)
        #print("\n", bst2)

        self.assertTrue(bst1 != bst2)

        bst3 = MyBSTMap()
        bst4 = MyBSTMap()

        bst3.put(0, '0')
        bst3.put(2, '2')

        bst4.put(0, '0')
        bst4.put(1, '1')
        self.assertTrue(bst1 != bst2)

        print("test_notequal_multiplenodes_difshapes OK")


    def test_notequal_multiplenodes_difkvs(self):
        """tests if 2 BSTs are different even if they have the same shape but different key:value pairs"""
        L = []
        for i in range(8, 0, -1):
            L.append((i, str(i)))

        bst1 = MyBSTMap()
        bst2 = MyBSTMap()

        for i in L:
            bst1.put(i[0], i[1])


        L2 = []
        for i in range(9, 17): #9 through 16
            L2.append((i, str(i)))

        for i in L:
            bst2.put(i[0], i[1])
            

        self.assertTrue(bst1 == bst2)
        print("test_notequal_multiplenodes_difkvs OK")


    def test_frompreorder_small(self):
        """tests to make sure the preorder method is outputting the correct value pair"""
        '''
                3:'3'
                /
            1:'1'
            / |
        0:'0' 2:'2'
        Traversals of this tree yields the following lists of k:v tuples:
        pre-order: [(3,'3'), (1,'1'), (0,'0'), (2,'2')]'''

        L = [(3,'3'), (1,'1'), (0,'0'), (2,'2')]
        
        bst = MyBSTMap.frompreorder(L)
        #print("\n")
        #print(bst)
        self.assertTrue(bst.root, BSTNode(3, '3')) #root
        self.assertTrue(bst.root.left, BSTNode(1, '1')) #root's left
        self.assertTrue(bst.root.right is None) #root's right
        self.assertTrue(bst.root.left.left, BSTNode(0, '0')) #lv2 left
        self.assertTrue(bst.root.left.right, BSTNode(2, '2')) #lv2 right
        self.assertTrue(bst.root.left.left.left is None) #lv 3
        self.assertTrue(bst.root.left.left.right is None) #lv 3

        '''
                  4:'4'
                  /   |
            3:'3'     5:'5'
              |         |
           1:'1'        7:'7'
           /  |         / |
        0:'0' 2:'2' 6:'6' 8:'8'
        '''
        L = [(4,'4'), (3,'3'), (1,'1'), (0,'0'), (2,'2'), (5,'5'), (7,'7'), (6,'6'), (8,'8')] #-----------might be wrong
        
        bst = MyBSTMap.frompreorder(L)
        #print("\n", bst)
        self.assertTrue(bst.root, BSTNode(4, '4')) #root
        self.assertTrue(bst.root.left, BSTNode(3, '3')) # lv 2 left
        self.assertTrue(bst.root.left.left, BSTNode(1, '1')) # lv 2 right
        self.assertTrue(bst.root.left.right is None) # lv 3 left node right: none
        self.assertTrue(bst.root.left.left.left, BSTNode(0, '0')) # lv3 left
        self.assertTrue(bst.root.left.left.right, BSTNode(2, '2')) #lv3 left most right
        self.assertTrue(bst.root.right, BSTNode(5, '5')) #lv2 right
        self.assertTrue(bst.root.right.left is None) # lv3 right most left
        self.assertTrue(bst.root.right.right, BSTNode(7, '7')) # lv3 right most
        self.assertTrue(bst.root.right.right.left, BSTNode(6, '6')) # lv4 right most left
        self.assertTrue(bst.root.right.right.right, BSTNode(8, '8')) #lv4 right most

        print("test_frompreorder_small OK")
        

    def test_frompreorder_large(self):
        """tests to make sure the preorder method is outputting the correct value pair, large BST"""
        '''Then, compare two large random trees (at least 100 nodes) --------------------------------------------important !!!!!!
        Then, compare two large random trees (at least 100 nodes)
        a) create a tree using randomly generated keys (use the random module)
        b) create a list of k:v pairs using preorder traversal
        c) create a new tree using that list MyBSTMap.frompreorder()
        d) verify the two trees are equal
        e) modify one of the trees
        f) verify the two trees are no longer equal.
        '''
        BST = MyBSTMap()
        BST1 = MyBSTMap()
        L = []
        for i in range(100):
            temp = random.randint(0, 100)
            L.append((temp, str(temp)))

        BST.frompreorder(L)
        #print("\n", bst)
        BST1.frompreorder(L)
        #print("\n", bst1)
        self.assertTrue(BST == BST1)

        BST2 = MyBSTMap().frompreorder(L[:-2])

        #print("\n", BST)
        #print("\n", BST2)

        self.assertTrue(BST != BST2)

        print("test_frompreorder_large OK")
        

    def test_frompostorder_small(self):
        """tests to make sure the postorder method is outputting the correct value pair"""
        '''
                3:'3'
                /
            1:'1'
            / |
        0:'0' 2:'2'
        Traversals of this tree yields the following lists of k:v tuples:
        post-order: [(0,'0'), (2,'2'), (1,'1'), (3,'3')]'''

        L = [(0,'0'), (2,'2'), (1,'1'), (3,'3')]
        
        bst = MyBSTMap.frompostorder(L)
        #print("\n", bst)

        self.assertTrue(bst.root, BSTNode(3, '3')) #root
        self.assertTrue(bst.root.left, BSTNode(1, '1')) #root's left
        self.assertTrue(bst.root.right is None) #root's right
        self.assertTrue(bst.root.left.left, BSTNode(0, '0')) #lv2 left
        self.assertTrue(bst.root.left.right, BSTNode(2, '2')) #lv2 right
        self.assertTrue(bst.root.left.left.left is None) #lv 3
        self.assertTrue(bst.root.left.left.right is None) #lv 3

        '''
                  4:'4'
                  /   |
            3:'3'     5:'5'
              |         |
           1:'1'        7:'7'
           /  |         / |
        0:'0' 2:'2' 6:'6' 8:'8'
        '''
        L = [(0,'0'), (2,'2'), (1,'1'), (6,'6'), (8,'8'), (7,'7'), (3,'3'), (5,'5'), (4,'4')] #-----------might be wrong
        
        bst = MyBSTMap.frompostorder(L)
        #print("\n", bst)
        self.assertTrue(bst.root, BSTNode(4, '4')) #root
        self.assertTrue(bst.root.left, BSTNode(3, '3')) # lv 2 left
        self.assertTrue(bst.root.left.left, BSTNode(1, '1')) # lv 2 right
        self.assertTrue(bst.root.left.right is None) # lv 3 left node right: none
        self.assertTrue(bst.root.left.left.left, BSTNode(0, '0')) # lv3 left
        self.assertTrue(bst.root.left.left.right, BSTNode(2, '2')) #lv3 left most right
        self.assertTrue(bst.root.right, BSTNode(5, '5')) #lv2 right
        self.assertTrue(bst.root.right.left is None) # lv3 right most left
        self.assertTrue(bst.root.right.right, BSTNode(7, '7')) # lv3 right most
        self.assertTrue(bst.root.right.right.left, BSTNode(6, '6')) # lv4 right most left
        self.assertTrue(bst.root.right.right.right, BSTNode(8, '8')) #lv4 right most


        print("test_frompostorder_small OK")


    def test_frompostorder_large(self):
        """tests to make sure the postorder method is outputting the correct value pair, large"""
        '''Then, compare two large random trees (at least 100 nodes)
        Then, compare two large random trees (at least 100 nodes)
        a) create a tree using randomly generated keys (use the random module)
        b) create a list of k:v pairs using postorder traversal
        c) create a new tree using that list MyBSTMap.frompostorder()
        d) verify the two trees are equal
        e) modify one of the trees
        f) verify the two trees are no longer equal.
        '''

        BST = MyBSTMap()
        BST1 = MyBSTMap()
        L = []
        for i in range(100):
            temp = random.randint(0, 100)
            L.append((temp, str(temp)))

        BST.frompostorder(L)
        print("\n", BST)
        BST1.frompostorder(L)
        print("\n", BST1)
        self.assertTrue(BST == BST1)

        BST2 = MyBSTMap().frompostorder(L[:-2])

        #print("\n", BST)
        #print("\n", BST2)

        self.assertTrue(BST != BST2)

        print("test_frompostorder_large OK")
        


unittest.main()