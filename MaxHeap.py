class Entry:
    def __init__(self, priority, item):
        """Entry object with a priority list and item value (any object)"""
        
        self.priority = priority #this is a list
        self.item = item #this is an object, of any type


    def __gt__(self, other):
        """if the priority is greater than other, if the same then if the item is greater than other"""
        # supports an arbitrary number of different priorities

        len1 = len(self.priority) #length of self priority list
        len2 = len(other.priority) #length of other priority list

        shorter = min(len1, len2) #find smaller of the 2 legnths

        i = 0 #starting at 0, with while loop going to end of smaller list
        while i < shorter:
            if self.priority[i] == other.priority[i]:
                i+=1
                continue
            return self.priority[i] > other.priority[i]
        #if the list is 
        return i < len1


    def __eq__(self, other):
        """if the priorities are equal, then the entry is equal, ignoring the fact if the items are different"""
        return self.priority == other.priority
    
    
    # repr is provided for you
    def __repr__(self):
        """Returns string representation of an Entry """
        return f"Entry(priority={self.priority}, item={self.item})"


class MaxHeap:
    # init is provided for you, but you should modify the default `heapify_direction` value
    def __init__(self, items=None, heapify_direction='down'):
        """Initializes a new MaxHeap with optional collection of items"""
        self._L = []
        
        # if a collection of items is passed in, heapify it
        if items is not None:
            self._L = list(items)
            if heapify_direction == 'up': self._heapify_up()

            elif heapify_direction == 'down': self._heapify_down()

            else: raise RuntimeError("Replace `heapify_direction` default with 'up' or 'down' instead of `None`")

        self.heap_size = len(items)


    def _heapify_up(self):
        """Heapifies self._L in-place using only upheap"""
        #starts top, heapify each value in list
        n = len(self._L)
        for i in range(n):
            self._upheap(i)


    def _heapify_down(self):
        """Heapifies self._L in-place using only downheap"""
        #move largest values in root, (i = 0) and smallest to tail end
        #if parent are smaller than child, swap
        #assume max heap
        
        n = len(self._L)
        for i in reversed(range(n)):
            self._downheap(i) 



    def put(self, entry):
        """adds an Entry to the list, then orders the list to maintain a heap"""
        self._L.append(entry) #add entry to list
        self._heapify_up() #move added entry as needed to maintain maxheap


    def remove_max(self):
        """removing the root in the max heap"""
        L = self._L 
        if len(self._L) <= 0:
            raise RuntimeError("can not remove from empty maxHeap")

        item = L[0].item #storing item to return at end
        L[0] = L[-1] #swap root with last ele in list
        L.pop()
        self._downheap(0)
        return item

    # len is number of items in PQ
    def __len__(self):
        """Number of items in PQ"""
        return len(self._L)


    def _upheap(self, i):
        """upheaps a single element in a list"""
        L = self._L
        parent = (i-1)//2
        if i > 0 and L[i] > L[parent]:
            self._swap(i, parent)
            self._upheap(parent)


    def _downheap(self, i):
        """downheap for max heap"""
        L = self._L
        children = self._children(i)
        if children:
            child = max(children, key = lambda x: L[x])
            if L[child] > L[i]:
                self._swap(i, child)
                self._downheap(child)
    

    def _children(self, i):
        """finds the children of the given index"""
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._L), right + 1))


    def _swap(self, a, b):
        """swaps 2 elements at the given indices"""
        L = self._L
        L[a], L[b] = L[b], L[a]





        #===========================#===========================#===========================
    
    def max_heapify(self, i):
        l = i*2
        r = i*2+1
        largest = i
        if l < self.heap_size and self._L[l] > self._L[i]:
            largest = l
        if r < self.heap_size and self._L[r] > self._L[largest]:
            largest = r
        if largest != i:
            temp = self._L[i]
            self._L[i] = self._L[largest]
            self._L[largest] = temp
            self.max_heapify(largest)


    def build_max_heap(self):
        self.heap_size = len(self)
        for i in range(len(self)//2, 1, -1):
            self.max_heapify(i)

    def heapSort(self):
        self.build_max_heap()
        for i in range(len(self), 2, -1):
            temp = self._L[i]
            self._L[i] = self._L[1]
            self._L[1] = temp
            self.heap_size -=1
            self.max_heapify(1);

