from AdjGraph import AdjacencySet

class Graph(AdjacencySet):
    def dfs(self, v):
        tree = {v:None} #child:parent
        return self._dfs(v, tree)
    
    def _dfs(self, v, tree):
        for n in self._neighbors(v):
            if n not in tree:      # haven't visited n yet
                tree[n] = v        # v is the parent of n
                self._dfs(n, tree) # continue dfs search with n before exploring v's neighbors

        return tree

    def dfs_iter(self, v):
        tree = {}              # empty dict for child:parent
        to_visit = [(None, v)] # (parent, child) tuples we want to explore

        while to_visit:
            a, b = to_visit.pop() # take *last* edge in to_visit
            if b not in tree:     # have not visited b yet
                tree[b] = a       # store a-->b in our tree
                for n in self._neighbors(b):
                    to_visit.append((b, n)) # add all of b's neighbors to to_visit

        return tree

    def bfs_iter(self, v):
        tree = {}              # empty dict for child:parent
        to_visit = [(None, v)] # (parent, child) tuples we want to explore

        while to_visit:
            a, b = to_visit.pop(0) # take *first* edge in to_visit
            if b not in tree:     # have not visited b yet
                tree[b] = a       # store a-->b in our tree
                for n in self._neighbors(b):
                    to_visit.append((b, n)) # add all of b's neighbors to to_visit

        return tree
if __name__ == '__main__':
    # 1-->2-->3-->4-->5
    # ^           |
    # +-----------+


    vs = {1, 2, 3, 4, 5}
    es = {(1,2), (2,3), (3,4), (4,1), (4,5)}

    g = Graph()
    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)

    print("dfs(2): {}".format(g.dfs(2)))
    print("dfs_iter(2): {}".format(g.dfs_iter(2)))
    print("bfs_iter(2): {}".format(g.bfs_iter(2)))


    # 1-->2-->3
    # V
    # 4-->5-->6
    # V
    # 7-->8-->9

    # dfs:
    # None->1->4->7->8->9
    #       |  |
    #       |  +->5->6
    #       +->2->3

    # bfs:
    # None->1->2->3
    #       |
    #       +->4->5->6
    #          |
    #          +->7->8->9 
    g = Graph()
    vs = {1,2,3,4,5,6,7,8,9}
    es = {(1,2), (2,3),
          (1,4), (4,5), (5,6),
          (4,7), (7,8), (8,9)}
    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)
    print()
    print("dfs_iter(1): {}".format(g.dfs_iter(1)))
    print("bfs_iter(1): {}".format(g.bfs_iter(1)))
