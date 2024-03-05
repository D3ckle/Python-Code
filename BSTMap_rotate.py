from BSTNode_rotate import BSTNode

class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root:
            self.root = self.root.put(key, value)
        
        else:
            self.root = BSTNode(key, value)

    def get(self, key):
        if self.root:
            return self.root.get(key).value
        
        raise KeyError("key {} is not in BSTMap".format(key))

    def __str__(self):
        if self.root:
            return self.root.print_subtree()
        
        else: return "Empty BST"

if __name__ == '__main__':
    import random
    #random.seed(658)
    n = 7
    bst = BSTMap()
    for i in range(n):
        k = random.randint(0, 99)
        #k = i
        print("putting {}".format(k))
        bst.put(k, str(k))
    print(bst)