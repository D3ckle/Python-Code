class EdgeSet:
    def __init__(self):
        self.V = set()
        self.E = set()

    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        self.E.add(e)

    def remove_edge(self, e):
        self.E.remove(e)

    def __iter__(self):
        return iter(self.V)

    def _neighbors(self, v):
        # neighbor of v if edge (v, ?) is in self.E
        nbrs = set()
        for e in self.E:
            if e[0] == v: nbrs.add(e[1])

        return nbrs

class Graph(EdgeSet):
    pass

if __name__ == '__main__':
    # Store the following graph:
    # 1--4
    # |\ |
    # | \|
    # 2--3

    g = Graph()
    vs = {1, 2, 3, 4}
    es = {(1,2), (1,3), (1,4),
          (2,1), (2,3),
          (3,1), (3,2), (3,4),
          (4,1), (4,3)}

    for v in vs: g.add_vertex(v)
    for e in es: g.add_edge(e)

    for v in g:
        print("v = {}, neighbors:".format(v))
        for nbr in g._neighbors(v):
            print("\t{}".format(nbr))
        print()
