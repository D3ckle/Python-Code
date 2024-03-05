#Interactive heap module that runs in terminal. Displays ASCII art of heaps as
#you add/remove items, including the up- and down-heaping steps.
#File is made to be run via terminal: python PriorityQueue_Interactive.py
#Main loop in:    if __name__ == '__main__' block.
#
#Jake Scoggin
import random
import time
from os import system
from os import name

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority
        
    def __repr__(self):
        return 'Entry({0.item}, {0.priority})'.format(self)        
        
class PQ:
    def __init__(self):
        self._L = []
        self._len = 0
    
    def _parent(index):
        #returns index of parent node
        return (index -1) // 2

    def _left(index):
        #returns index of left child
        return index * 2 + 1

    def _right(index):
        #returns index of right child
        return index * 2 + 2
        
    def insert(self, item, priority):   
        #adds item to priority queue
        to_print = 'Adding ' + str(priority) +'...'
        self._update(to_print, sleep_time)

        self._L.append(Entry(item, priority))
        self._len += 1
        
        to_print += ' Added'
        self._update(to_print, sleep_time)
        
        self._upheap(len(self._L)-1, priority)
               

    
    def find_min(self):
        return self._L[0]
        
    def _upheap(self, index, priority_added, switch_string = None):
        if switch_string is None: switch_string = ''
        if index == 0: return
        else:
            i_parent = PQ._parent(index)
            i_child = index        
            if self._L[i_child] < self._L[i_parent]:
                switch_string += '\nSwitching {0.priority} and {1.priority}...'.format(self._L[i_child], self._L[i_parent])
                self._update(switch_string, sleep_time)
                self._L[i_parent], self._L[i_child] = self._L[i_child], self._L[i_parent]
                switch_string += ' Switched {1.priority} and {0.priority}'.format(self._L[i_child], self._L[i_parent])
                self._update(switch_string, sleep_time)
                self._upheap(i_parent, priority_added, switch_string)
    
   
            
    def __repr__(self):
        return str(self._L)
        
    def priority_list(self):
        L = []
        for entry in self._L:
            L.append(entry.priority)
        return L
    
    def __len__(self):
        return self._len
    
    def print_heap(self):
        #Prints the heap in ASCII art
        n_items_bottom = 1
        n_levels = 1
        while n_items_bottom <= 1/2 * len(self):
            n_items_bottom *= 2
            n_levels += 1
        width_bottom = int(n_items_bottom * 10/2 - 2)

        w_buffer = (width_bottom-2)//2
        for level in range(n_levels):
            symbol_string = ''
            number_string = ''
            for j in range(2**level):
                if 2**level + j >len(self._L):
                    print(symbol_string)
                    print(number_string)
                    return
                
                if j == 0:
                    number_string += ' ' * w_buffer
                    if level>0: symbol_string += ' ' * (w_buffer+1)                   
                else: 
                    number_string += ' ' * (w_buffer*2+2)
                    if level>0: symbol_string += ' ' * (w_buffer*2+2)
                
                if level > 0: 
                    if j % 2:
                        if level == n_levels-1:
                            symbol_string += '  '
                            number_string += '  '
                        symbol_string += '\\  '
                        
                    else: symbol_string += '/'
                number_string += '{:02d}'.format(self._L[2**(level)+j-1].priority)
                if level == 0: number_string += ' <--root'
            print(symbol_string)
            print(number_string)
            
            
            if level != n_levels -1: 
                w_buffer = (w_buffer-2) // 2
                n_underscores = ((w_buffer*2+2 - 4)//2)
                symbol_string = ''
                for j in range(2**level):
                    if j == 0:
                        symbol_string += ' ' * (w_buffer+2) + '_' * n_underscores + '/  \\' + '_' * n_underscores
                        
                    else:
                        symbol_string += ' ' * (w_buffer*2+2+2+2) + '_' * n_underscores + '/  \\' + '_' * n_underscores
                print(symbol_string)
                
    def _update(self, to_print, sleep_time=None):
        clear()
        print('Binary Heap Tree'.center(40,'*'))
        self.print_heap()
        print()
        print('Heap as List'.center(40,'*'))
        print(self.priority_list())
        print()
        print(to_print)
        if sleep_time:
            time.sleep(sleep_time)
        else:
            input()

# clear is used before printing a new heap in terminal
def clear(): 
    if name == 'nt':
        system('cls') 
    else:
        system('clear')
        
            
        
                
if __name__ == '__main__':
    random.seed(658)    
    
    #sleep_time = 0.5 # wait a fixed time before progressing
    sleep_time = None # wait for user to press enter before progressing


    n = 15
    pq = PQ()
    #priorities = [24, 32, 54, 62, 42, 68, 65, 51, 67, 49, 92, 72, 86, 76, 75]
    
    
    for i in range(n):
        pq.insert(item = i, priority = random.randint(0, 99)) 
    

    for i in range(n):
        pq.remove_min() 
