#from time_functions import time_f
                    
def bigO_1(n, decimal=2):
    """rounds a number to a specific decimal place"""
    temp = 10**decimal#-----------2, exponent, assign
    return round(n*temp)/temp #---4 multiplication, round, division, return
    #2 + 4 = 6 = O(1)

def bigO_n(n, step=1):
    """adds the specified value to each item in the list n"""
    for i in n: #---n
        i += step#--2
    #n(2)= O(1)

def bigO_n2t2(x, y):
    """tries to find a duplicate values from both lists x and y"""
    for i in x: #-------------n
        for j in y:#----------n
            if (i == j): #----1
                return True #-1
    return False#-------------1
    #n(n(1+1)) +1 = O(n^2)

def search_list(List, value):
    return value in List == True

def search_Tuple(tupl, value):
    return value in tupl == True

def search_str(str, value):
    return value in str == True

def search_set(set, value):
    return value in set == True