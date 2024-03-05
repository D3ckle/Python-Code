class Graph:
    def __init__(self, V=set(),E=set()):
        """initializes a graph with specified parameters:
        V = a tuple of vertices
        E = a set of tuple edges connecting the vertices together"""
        self.Dict = dict() #dictionary of dictionaries

        for v in V:
            self.Dict[v] = {} #adding a default diction at each dictionary
            for (u,p,wt) in E: #unpacking the edges: vertex, vertex, distance
                if u == v: self.Dict[v][p] = wt
                if p == v: self.Dict[v][u] = wt 
        
    def add_vertex(self, v):
        """Adds another vertex to the dictionary, another dictionary will be added to self.Dict"""
        self.Dict[v] = {}

    def remove_vertex(self, v):
        """removes the specified vertex (v) from self.Dict"""
        try:
            del self.Dict[v]
        except: raise KeyError("vertex ", v, " not in graph")

    def add_edge(self, u, v, wt):
        """Adds an edge between 2 vertices (u and v), with the given weight (wt) to self.dict at each dict location"""
        self.Dict[u][v] = wt
        self.Dict[v][u] = wt

    def remove_edge(self, u, v, wt):
        """removes the speciifed edge between vertices u and v with weight (wt) from self.Dict at each vertex location"""
        try:
            del self.Dict[u][v]
            del self.Dict[v][u]
        except: raise KeyError("vertex ", v, " not in graph")

    def nbrs(self, v):
        """returns an iterator over the v's"""
        return iter(self.Dict[v])

    def wt(self, u, v):
        """returns the weight of the edge conneceting the 2 cities (vertices: u, v)"""
        return self.Dict[u][v]

    def __iter__(self):
        """the iterator of the graph"""
        return iter(self.Dict)

    def __len__(self):
        """returns the length of the dictionary"""
        return len(self.Dict)

    def vertices(self):
        """returns all vertices in the dictionary"""
        return iter(self.Dict)


    """=========================================================================="""
    """================================traversals================================"""
    """=========================================================================="""

    def fewest_flights(self, city): 
        """finds how to get from city to any other city in the graph with the fewest
        number of flights: bfs"""
        tree = {city:None}
        d = {u:float('inf') for u in self.vertices()} #all other distances will be known as 'inf' since we will calc the distances as alg progresses
        d[city] = 0 #distance from start is always 0
        q = Queue() #queue to add vertices to when we traverse the graph
        q.enqueue(city) #add starting city
        while len(q) != 0: #as we progress, we will keep adding cities (vertices) 
            v = q.dequeue() #remove vertex
            for nbr in self.nbrs(v): #checks the neighbors
                if nbr not in tree:
                    tree[nbr] = v
                    q.enqueue(nbr) #if nbr found not in queue, add it to the queue
                    d[nbr] = d[tree[nbr]] + 1
        return tree, d


    def shortest_path(self, city):
        """ finds how to get from city to any other city in the graph with the fewest
        number of miles travelled - this is for environmentally concious users who want to use the least
        amount of fuel to get between two cities"""
        #uses the dijkstra alg as a basis
        tree = {}
        d = {}
        tovisit = PriorityQueue()
        tovisit.insert((None, city), 0) #adding the starting vertex to priority queue
        a = ""
        for u, v in tovisit: #comparing vertices
            if v not in tree:
                tree[v] = u
                if u is None:
                    d[v] = 0
                    M = float('inf')
                    for e in self.nbrs(v):
                        if e != v and self.wt(e,v) < M:
                            m = e  
                            M = self.wt(e,v)
                    d[m] = self.wt(v, m)
                    a = m
                    for n in self.nbrs(m):
                        if n != v:
                            tovisit.insert((m,n), self.wt(m,n))
                else:
                    d[v] = d[u] + self.wt(v, u)
                    for e in self.nbrs(v):
                        if e != v and e != u:
                            tovisit.insert((v,e), self.wt(v,e))
        tree[a] = city
        return tree, d


    def minimum_salt(self, city):
        """ connects city to every other city in the graph with the fewest total
        number of miles - this tree would allow us to keep all cities connected in the winter with the least
        amount of salt used on roads: Prim alg"""
        tree = {}
        D = {}
        tovisit = PriorityQueue()
        tovisit.insert((None, city), 0) #adding the starting vertex to priority queue
        a = ""
        for u, v in tovisit:
            if v not in tree:
                tree[v] = u
                if u is None:
                    D[v] = 0
                    M = float('inf')
                    for e in self.nbrs(v):
                        if e != v and self.wt(e,v) < M:
                            m = e  
                            M = self.wt(e,v)
                    D[m] = self.wt(v, m)
                    a = m
                    for n in self.nbrs(m):
                        if n != v:
                            tovisit.insert((m,n), self.wt(m,n))
                else:
                    D[v] = self.wt(u, v)
                    for e in self.nbrs(v):
                        if e != v and e != u:
                            tovisit.insert((v,e), self.wt(v,e))
        tree[a] = city
        return tree, D 


#==============================================================================================================

class Entry:
    """object with an item value and a priority value"""
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        """return True if self has a lower priority than other, False otherwise."""
        return self.priority < other.priority
    
    def __repr__(self):
        """helps to have a repr method for debugging"""
        return f"Entry(item={self.item}, priority={self.priority})"

    def __iter__(self):
        """iterator of the entry class"""
        return iter(self.item)

    def __eq__(self, other): 
        """returns True if the two entries have the same priority and item."""
        return self.item == other.item and self.priority == other.priority 

#==============================================================================================================

class PriorityQueue:
    """creates a priority queue that has values with priorities"""
    def __init__(self, entries=[]):
        self.l = []
        for e in entries: self.insert(e[0],e[1]) #better for formating to add individually to maintain format 
                                                 #of a queue

    def __len__(self):
        """call list len magic method for length of the priority queue"""
        return len(self.l)

    def insert(self, item, priority):
        """adds item with given priority to priority queue"""
        self.l.append(Entry(item, priority)) #add the item

    def find_min(self):
        """returns (but does not remove) the item with minimum priority."""     
        Min = self.l[0] #min entry
        for i in range (1, len(self.l)): #search the rest of the list for the smallest entry
            if self.l[i] < Min:
                Min = self.l[i]
        return Min #return the item with the minimum entry

    def __iter__(self):
        """iter of the prio que, uses list iter"""
        return iter(self.l)

    def remove_min(self):
        """returns and removes the item with minimum priority. This means an item with priority 0 will be returned before an 
        item with priority 5, for instance."""
        min_entry = min(self.l) 
        self._L.remove(min_entry)
        return min_entry

#==============================================================================================================

class Queue:
    """a simple queue, w/o priority if prio is not needed"""
    def __init__(self): 
        self.L = list() #better than []
    
    def enqueue(self,item):
        """adding a value to the end of the list"""
        self.L.append(item)

    def dequeue(self):
        """removing a value from the beginning of the list"""
        return self.L.pop(0)

    def __len__(self):
        """return the length of the list"""
        return len(self.L)
