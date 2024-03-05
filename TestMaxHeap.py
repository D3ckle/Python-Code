from MaxHeap import Entry, MaxHeap
import unittest, random, time
random.seed(658)

#TODO: Fill out any empty tests below
class TestEntry(unittest.TestCase):

    def entry_init(self):
        e = Entry()

        e1 = Entry(priority=[], item = 0)

        self.assertEqual(e1.priority, [])
        self.assertEqual(e1.item, 0)

        print("entry_init OK")

    def test_gt_onepriority(self):
        """Tests Entry's with 1 priority"""
        e1 = Entry(priority=[0], item="jake") # 1 level priority
        e2 = Entry(priority=[1], item="rachel")
        self.assertTrue(e2 > e1) # 1 > 0

        e1 = Entry(priority=[1, "a"], item="jake") # 2 levels priority
        e2 = Entry(priority=[1, "b"], item="rachel")
        e3 = Entry(priority=[0, "c"], item="tobias")
        self.assertTrue(e2 > e1) # 1==1, 'b' > 'a'
        self.assertTrue(e2 > e3)  # 1 > 0

        e1 = Entry(priority=[0], item=0)
        e2 = Entry(priority=[0], item=1)
        self.assertFalse(e2 > e1)  # same list so one can not be greater than the other


        print("test_gt_onepriority OK")


    def test_gt_threepriorities(self):
        """Tests Entries with with 3 priorities"""
        e1 = Entry(priority=[0, "a", 3.72], item="jake") # 3 levels priority
        e2 = Entry(priority=[0, "a", 4.73], item="rachel")
        self.assertTrue(e2 > e1) # 0==0, 'a'=='a', 4.73 > 3.72

        e1 = Entry(priority=[0, 1, 2], item=1) # 3 levels priority
        e2 = Entry(priority=[0, 1, 2], item=2)
        self.assertFalse(e2 > e1) # 0==0, 1==1, 2==2, not greater

        print("test_gt_threepriorities OK")



    def test_gt_mismatchedpriorities(self):
        """Test comparisons b/w entries with different numbers of priorities"""

        e1 = Entry(priority=[], item=0)
        e2 = Entry(priority=[0], item=0)
        self.assertTrue(e2 > e1) #0 > None

        e1 = Entry(priority=[0, 1, 0], item=1) # 3 levels priority
        e2 = Entry(priority=[0, 1], item=2)
        self.assertTrue(e1 > e2) # 0==0, 1==1, 0 > None, true

        print("test_gt_mismatchedpriorities OK")


    def test_eq(self):
        """Test that items w/ exact same priorities are seen as equal"""
        e1 = Entry(priority=[0, 1], item=1)
        e2 = Entry(priority=[0, 1], item=2)
        self.assertEqual(e1, e2) #priorities equal, but items are not; still equal

        e1 = Entry(priority=[0], item=1)
        e2 = Entry(priority=[0], item=2)
        self.assertEqual(e1, e2)
        e3 = Entry(priority=[], item=3)
        self.assertFalse(e3==e2) #[] != [0]


        print("test_eq OK")


class TestMaxHeap(unittest.TestCase):
    def test_add_remove_single(self):
        """Add a single item to the max heap, then remove it. This test is provided for you as an example."""
        e1 = Entry(priority=[0], item="jake")
        mh = MaxHeap()
        self.assertEqual(len(mh), 0)
        mh.put(e1)
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove_max(), "jake")

        print("test_add_remove_single OK")


    def test_add_remove_random(self):
        """Add and remove many random items w/ same number of priorities"""
        n = 100#0
        
        mh = MaxHeap()
        self.assertEqual(len(mh), 0)
        for i in range(n):
            mh.put(Entry(priority=[0], item=random.randint(0, 100)))


        self.assertEqual(len(mh), n)

        for i in range(n):
            item = mh._L[0].item
            self.assertEqual(mh.remove_max(), item)

        print("test_add_remove_random OK")


    def test_add_remove_several(self):
        """Add and remove several items with different numbers of priorities"""
        n = 100#0
        
        mh = MaxHeap()
        self.assertEqual(len(mh), 0) #initialize: len = 0

        for i in range(n): #adding n entries
            prio = []
            for i in range(random.randint(0, 10)): #creating a rand list of rand prio's for each entry
                prio.append(random.randint(0, 100))

            mh.put(Entry(priority=prio, item=random.randint(0, 100))) #adding n entries with diff. priorities


        self.assertEqual(len(mh), n) #added n entries to list, len = n

        

        for i in range(n): #removing and asserting true each entry
            item = mh._L[0].item

            self.assertEqual(mh.remove_max(), item)

        print("test_add_remove_several OK")



    def test_removefromempty(self): #-------------------------------------------------------------------?????? do we time the function, its empty so should it do ntohing?
        """Test Runtime error when removing from empty"""

        mh = MaxHeap()
        self.assertEqual(len(mh), 0) #initialize: len = 0

        with self.assertRaises(RuntimeError):
            mh.remove_max()


        self.assertEqual(len(mh), 0)

        print("test_removefromempty OK")


    # NOTE: This times heapify_up and _down, but does not test their functionality
    def test_heapify(self):
        """Times heapify up and heapify down approaches. This 'test' provided for you"""
        print() # an extra blank line at the top
        
        # table header
        print('='*40)
        print(f"{'n':<10}{'t_h_up (ms)':<15}{'t_h_down (ms)':<15}"   )
        print('-'*40)

        # table body
        scalar = int(1E3)
        for n in [i*scalar for i in [1, 2, 3, 4, 5]]:
            t_h_up = 1000*time_f(MaxHeap, (list(range(n)), 'up'))
            t_h_down = 1000*time_f(MaxHeap, (list(range(n)), 'down'))
            print(f"{n:<10}{t_h_up:<15.2g}{t_h_down:<15.2g}")

        # table footer
        print("-"*40)

def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        if end-start < t_min: t_min = end - start
    return t_min

unittest.main()

