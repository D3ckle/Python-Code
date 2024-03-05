# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests


class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0):
        """initializer for the local record class"""
        self.pos = (round(pos[0], precision), round(pos[1], precision))# a tuple representing the latitude and 
        #longitude of this record. Incoming weather reports will have arbitrary precision, but any that round to 
        #the same (lat, long) should be equal, so you'll need to round before storing
        
        self.max = max
        self.min = min

        self.precision = precision #to what decimial is the items rounded to

    def add_report(self, temp): 
        """Updates max and min if appropriate"""
        #temp = tempurature

        if self.max is None or temp > self.max: #new max tempurature
            self.max = temp
        if self.min is None or temp < self.min: #new min tempurature
            self.min = temp


    def __eq__(self, other):
        """returns True iff two records are for the same position"""
        #other = another LocalRecord

        if self.pos == other.pos:
            return True
        return False
        

    def __hash__(self):
        """ returns a hash for this object based on its position"""
        return hash(self.pos) #use tuple's hash method

    def __repr__(self):
        """prints information of the local record, redefines the print operation and how a localRecord is written on the console"""
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"


    #==============================================================================================================
    #==============================================================================================================



class RecordsMap:
    """Write a data structure RecordsMap that allows O(1) updating of a collection of records whenever a new
    report comes in. Keys should be a (lat, long) tuple and values should be a (min, max) tuple."""

    def __init__(self):
        """initializer"""
        self._n_buckets = 8              # initial size. Good to use a power of 2 here.
        self._len = 0                    # Number of items in custom set
        self._L = [[] for i in range(self._n_buckets)]   # List of empty buckets -adding localRecords here



    def __len__(self):
        """ the number of key:value pairs stored"""
        return self._len



    def add_report(self, pos, temp):
        """add_report(pos, temp) updates max and min temperature for the given position as appropriate.
        There are 2 inputs here, a 2xtuple for position and a float for tempurature"""
        #pos = tuple w/ 2 values
        #temp = tempurature to update the position's temp with
        LR = LocalRecord(pos, temp, temp) #creating a local record to allow for comparision
        index = hash(LR) % self._n_buckets

        for i in self._L[index]:
            if i == LR:
                i.add_report(temp)
                return

        self._len+=1 # update length only if there is a new position being added
        self._L[index].append(LR) # Add item to end of bucket
        # rehash if necessary (items >= 2*buckets)
        if self._len >= self._n_buckets//2: #use load factor, never want to have more than half length of list
            self._rehash(2*self._n_buckets)




    def __getitem__(self, pos):

        """returns a tuple of (min, max) temperatures for a given position.
        Raises KeyError if a point corresponding to the specified tuple is not in the mapping"""

        try:
            LR = LocalRecord(pos)
            index = hash(LR) % self._n_buckets #get location of where the bucket is
            #print(self._L[index])
            for item in self._L[index]: #looks for the LR in the bucket
                if item == LR:
                    return (item.min, item.max)
        except:
           KeyError("point corresponding to the specified tuple is not in the mapping")
        



    def __contains__(self, pos):
        """returns True (False) if a given position is (is not) in this RecordsMap. It's fine to
        pass arbitrary precision (lat, long) positions here, LocalRecord takes care of the rounding"""
        #for i in self._L[index]:
         #   if i == 
        index = hash(pos) % self._n_buckets

        if pos in self._L[index]:# return True if item is in bucket, false otherwise
            return True
        return False



    def _rehash(self, m_new):
        """periodically rehash as number of entries increases. Note that this is a private method
        you do not need to write a unittest for it. However, you should write a test to make sure you're O(1)
        for add_report/contains/get, to make sure this method is getting called correctly"""

        """Rehashes every item from a hash table with n_buckets to one with new_buckets. new_buckets will be either 2*n_buckets or 1/2*n_buckets, depending on whether we are reahshing up or down."""
        # Make a new list of `new_buckets` empty lists
        new_l = [[] for i in range(m_new)]
        self._n_buckets = m_new

        # Using a for loop, iterate over every bucket in self._L
        for bucket in self._L:
            #i is a list in the bucket
            # using a for loop, iterate over every item in this bucket
            for record in bucket:
                #j is the item in i, the list
                # Find the index of the new bucket for that item

                index = hash(record) % m_new
                # add that item to the correct bucket
                new_l[index].append(record)

        # Update self._L to point to the new list
        self._L = new_l
        print(self._L)