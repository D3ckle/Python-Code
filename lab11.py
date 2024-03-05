class Graph_ES:
    """"""

    def __init__(self, Vs= (), Es= ()):
        """Vs = set of vertices(int values), Es = , edges, a set of tuples"""

        self.Vs = set()
        self.Es = set()
        
        for v in Vs: self.add_vertex(v)
        for u,v in Es: self.add_edge((u, v))


    def remove_vertex(self, v):
        try:
            self.Vs.remove(v)
        except: raise KeyError
        
    def __iter__(self):
        return iter(self.Vs)

    def add_vertex(self, v):
        self.Vs.add(v)

    def _neighbors(self, v):
        return (w for u, w in self.Es if u == v)

    def add_edge(self, e):
        self.Es.add(e)

    def remove_edge(self, e):
        try:
            self.Es.remove(e)
        except: raise KeyError

    def __len__(self):
        return len(self.Vs)


#================================================================================================
#================================================================================================
#================================================================================================


class Graph_AS:
    """"""
    def __init__(self, Vs= (), Es= ()):
        """Vs = set of vertices(int values), Es = , edges, a set of tuples (int, int)"""

        self.Vs = set()
        self.Es = dict()
        
        for v in Vs: self.add_vertex(v)
        for u,v in Es: self.add_edge((u, v))


    def remove_vertex(self, v):
        try:
            self.Vs.remove(v)
        except: raise KeyError
        
    def __iter__(self):
        return iter(self.Vs)

    def add_vertex(self, v):
        self.Vs.add(v)

    def _neighbors(self, v):
        return iter(self.Es[v])

    def add_edge(self, e):
        a, b = e
        if a not in self.Es:
            self.Es[a] = {b}
        else:
            self.Es[a].add(b)


    def remove_edge(self, e):
        a, b = e

        self.Es[a].remove(b)
        if len(self.Es[a]) == 0:
            self.Es.pop(a)


    def __len__(self):
        return len(self.Vs)
        

#=================================================================================================



def dijkstra(self, v):
    tree = {}
    d = {v:0}
    to_visit = PriorityQueue()
    to_visit.insert((None, v), 0) #tuple(previous node, current node), distance

    for p, v in to_visit:
	    if v not in tree:
		    tree[v] = p
		    if p is not None:
			    d[v] = d[p] + self.weight(p, v)
		    for n in self.nbrs(v):
			    to_visit.insert((v,n), d[v] + self.weight(v,n))
	    return tree, d




def prim(self, v):
    """starts from source vertex, finds shortest path with no cycles (multiple paths to another node)"""
    tree = {}
    d = {v:0}
    to_visit = PriorityQueue()
    to_visit.insert((None, v), 0) #tuple(previous node, current node), distance

    for p, v in to_visit:
	    if v not in tree: 
		    tree[v] = p
		    if p is not None:
			    d[v] = self.weight(p, v)
		    for n in self.nbrs(v):
			    to_visit.insert((v,n), self.weight(v,n))
	    return tree, d









