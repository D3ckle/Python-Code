class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        """return True if self has a lower priority than other, False otherwise."""
        if self.priority < other.priority:
            return True
        return False
            

    def __eq__(self, other): 
        """returns True if the two entries have the same priority and item."""
        return self.item == other.item and self.priority == other.priority 


#==============================================================================================================


class PQ_UL:
    def __init__(self, l = []):
        self.l = l


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


    def remove_min(self):
        """returns and removes the item with minimum priority. This means an item with priority 0 will be returned before an 
        item with priority 5, for instance."""

        Min = 0 #index of the first : temp to become the index of the min entry
        for i in range (1, len(self.l)): #search the rest of the list for the smallest entry
            if self.l[i] < self.l[Min]:
                Min = i

        temp = self.l[Min]
        self.l.pop(Min)
        return temp #return the min Entry removed




#===========================================================================================================




class PQ_OL:
    #reverse sorted list (using sort function)
    def __init__(self, l = []):
        self.l = l
        self.l.sort(reverse = True) #min value at end and pop that off


    def __len__(self):
        """call list len magic method for length of the priority queue"""
        return len(self.l)


    def insert(self, item, priority):
        """adds item with given priority to priority queue"""
        self.l.append(Entry(item, priority)) #add the item
        self.l.sort(reverse = True) #sort the list after adding the item

    def find_min(self):
        """returns (but does not remove) the item with minimum priority."""     
        return self.l[-1] #-------------------------------------------------------- is sort method ordering by priority?
    

    def remove_min(self):
        """returns and removes the item with minimum priority. This means an item with priority 0 will be returned before an item with priority 5, for instance."""
        temp = self.find_min() #store variable to return after item is removed
        self.l.pop() #remove the last element since the reverse sorted list will have the min at the end
        return temp #return the min Entry removed

