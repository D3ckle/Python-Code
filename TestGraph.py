from Graph import Graph
import unittest

def ascii_art():
    print("san francisco--------486 miles------\_")
    print("        |                             \_")
    print("     215 miles                          \_")
    print("        |                                 \_")
    print("   santa Barbara-----95 miles__             \_")
    print("                               los angeles    \_")
    print("                                      |         \_")
    print("                                120 miles        palm springs")
    print("                                      |          |")
    print("                                     san diego ---139 miles")

    

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.

    '''
        san francisco--------486 miles----___
                |                            \_
             215 miles                         \_
                |                                \_   
          santa Barbara-----95 miles__             \_ 
                                      los angeles    \_
                                             |         \_
                                       120 miles        palm springs
                                             |              |
                                            san diego ---139 miles
    '''

    def setUp(self):
        """set up function for creating the initial graph"""
        self.V = {"san francisco", "santa Barbara", "los angeles", "san diego", "palm springs"}

        self.E = {("san francisco", "santa Barbara", 215), 
             ("santa Barbara", "los angeles", 95), 
             ("los angeles", "san diego", 120), 
             ("san diego", "palm springs", 139), 
             ("palm springs", "san francisco", 486)}

        self.g = Graph(self.V, self.E)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """set up function for creating the initial graph"""


        self.V = {"san francisco", "santa Barbara", "los angeles", "san diego", "palm springs"}
        self.E = {("san francisco", "santa Barbara", 215), 
             ("santa Barbara", "los angeles", 95), 
             ("los angeles", "san diego", 120), 
             ("san diego", "palm springs", 139), 
             ("palm springs", "san francisco", 486)}

        self.g = Graph(self.V, self.E)

        #self.assertEqual(self.Dict, self.V)

    def test_fewest_flights(self):
        """tests to make sure that the function finds the shortest route between cities from a starting city (unweighted)"""
        # construct dictionary of expected answers
        # fewest_flights - vertex:number_of_flights
        D_expected = {"san francisco":0, 
                      "santa Barbara":1, 
                      "palm springs":1, 
                      "los angeles":2, 
                      "san diego":2}
        '''
        tree, D = self.g.fewest_flights("san francisco") # run alg and return the two dictionaries

        # iterate over each vertex in graph, and make sure you got the correct answer
        for v in self.g: 
            self.assertEqual(D[v], D_expected[v])
        '''

    def test_shortest_path(self):
        """tests finds shortest route with fewest miles traveled from starting city"""
        # construct dictionary of expected answers
        # shortest_path - vertex:distance_from_source
        D_expected = {"san francisco":0, 
                      "santa Barbara":215, 
                      "los angeles":310, 
                      "san diego":430, 
                      "palm springs":569}

        tree, D = self.g.shortest_path("san francisco") # run alg and return the two dictionaries

        # iterate over each vertex in graph, and make sure you got the correct answer
        for v in self.g: 
            self.assertEqual(D[v], D_expected[v])

    def test_minimum_salt(self):
        """connects all cities with shortest path"""
        # construct dictionary of expected answers
        # minimum_salt - vertex:weight_used_to_visit_vertex
        D_expected = {"san francisco":0, 
                      "santa Barbara":215, 
                      "los angeles":95, 
                      "san diego":120,
                      "palm springs":139}

        tree, D = self.g.minimum_salt("san francisco") # run alg and return the two dictionaries

        # iterate over each vertex in graph, and make sure you got the correct answer
        for v in self.g: 
            self.assertEqual(D[v], D_expected[v])


unittest.main()