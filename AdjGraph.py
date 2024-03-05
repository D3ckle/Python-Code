class AdjacencySet:
    def __init__(self):
        self.V = set()
        self.nbrs = dict()

    def add_vertex(self, v):
        self.V.add(v)

    def add_edge(self, e):
        a, b = e # e = (node1, node2)
        
        if a not in self.nbrs:
            self.nbrs[a] = {b} #Opt 1
        # self.nbrs[b] = {a} #Opt 2
        else:
            self.nbrs[a].add(b)

    def remove_edge(self, e):
        a, b = e
        self.nbrs[a].remove(b)
        if len(self.nbrs[a]) == 0:
            self.nbrs.pop(a)

    def __iter__(self):
        return iter(self.V)

    def _neighbors(self, v):
        return iter(self.nbrs[v]) if v in self.nbrs else set()    
