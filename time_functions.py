from functions import bigO_1, bigO_n, bigO_n2t2, search_list, search_Tuple, search_str, search_set

#this currnt file is the mudle, so it does not recognize this as the functin to run off of
#import functions
import time

def time_f(func, args, n_trials=10):
    """returns the number of seconds to run func with args, but with an arbitrary number of """
    minVal = float('inf') #so the first iteration will always override the infinity
    for i in range(n_trials): #run the test multiple times for lowest in the trials
        start = time.time() #gets the time at the current moment during the program
        func(*args) #run function with unlimited args in a tuple
        if time.time()-start < minVal: #grab min value and compare 
            minVal = time.time() - start
    return minVal #show the lowest value that the func took to run


if __name__ == '__main__': #main function

    #the numbers used for how long the functions will execute, i.e. how long o a list the function needs to process, etc.
    n_1 = 10 #trial 1 iterations, runs n times
    n_2 = 100 #trial 2 iterations
    n_3 = 1000 #trial 3 iterations

    #function 1: rounding a number to a specified decimal
    tup1 = (1.23456789, 1) #round the number to the first decimal place
    #trial 1
    f1_1 = time_f(bigO_1, tup1) #time it takes to run function n times
    t1_1  = ("{:.3g} ms".format(f1_1*1000)) #calculate the time it takes to run the first function, str
    #trial 2
    f1_2 = time_f(bigO_1, tup1)
    t1_2  = ("{:.3g} ms".format(f1_2*1000))
    #trial 3
    f1_3 = time_f(bigO_1, tup1)
    t1_3  = ("{:.3g} ms".format(f1_3*1000))
   
    #function 2: modify the inputed list by adding to it
    #trial 1
    L2_1 = [i for i in range(n_1)] #creates a list that is the length of n
    tup2_1 = (L2_1, 2) #parameters for the function; adds to each value in the list
    f2_1 = time_f(bigO_n, tup2_1)
    t2_1= ("{:.3g} ms".format(f2_1*1000))

    #trial 2
    L2_2 = [i for i in range(n_2)]
    tup2_2 = (L2_2, 2)

    f2_2 = time_f(bigO_n, tup2_2)
    t2_2= ("{:.3g} ms".format(f2_2*1000))

    #trial 3
    L2_3 = [i for i in range(n_3)]
    tup2_3 = (L2_3, 2)

    f2_3 = time_f(bigO_n, tup2_3)
    t2_3= ("{:.3g} ms".format(f2_3*1000))

    #function 3 : checking 2 lists and seeinf if there is a value on one list that is the same in the other
    #trial 1
    l1_1 = [i for i in range(n_1)] #creates a list that is the length of n
    l2_1 = [] #empty list, will be filled in later
    for i in range(n_1): #making a second list with values following the previous list
        l2_1.append(i+n_1) #starting from n+1, with last value at n*2

    tup3_1 = (l1_1, l2_1) #parameters for function 3
    f3_1 = time_f(bigO_n2t2, tup3_1) #time it takes to run function 3
    t3_1 = ("{:.3g} ms".format(f3_1*1000)) #time to run func3, converted into a string

    #trial 2
    l1_2 = [i for i in range(n_2)]
    l2_2 = []
    for i in range(n_1):
        l2_2.append(i+n_2)

    tup3_2 = (l1_2, l2_2)
    f3_2 = time_f(bigO_n2t2, tup3_2)
    t3_2 = ("{:.3g} ms".format(f3_2*1000))

    #trial 3
    l1_3 = [i for i in range(n_3)]
    l2_3 = []
    for i in range(n_3):
        l2_3.append(i+n_3)

    tup3 = (l1_3, l2_3)
    f3_3 = time_f(bigO_n2t2, tup3)
    t3_3 = ("{:.3g} ms".format(f3_3*1000))

    #table
    variable_line = "|n" + "\t" + "O(1)" + "\t" + "O(n)" + "\t" + "O(n^2)\t|" #only the categories

    values_line_1 = str("|" + str(n_1) + "\t" + t1_1 + "\t" + t2_1 + "\t" + t3_1 + "\t|") #first row times, on n_1
    values_line_2 = str("|" + str(n_2) + "\t" + t1_2 + "\t" + t2_2 + "\t" + t3_2 + "\t|") #second row times, on n_2
    values_line_3 = str("|" + str(n_3) + "\t" + t1_3 + "\t" + t2_3 + "\t" + t3_3 + "\t|") #third row times, on n_3

    delim = "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" #fancy looking line
    line = "|-------------------------------|" #normal looking line

    #my table, time it takes to run my 3 functions 
    print(delim)
    print(variable_line)
    print(line)
    print(values_line_1)
    print(values_line_2)
    print(values_line_3)
    print(delim)

    print()

    '''
    n_1 = 10**5 #trial 1 iterations, runs n times
    n_2 = 10**6 #trial 2 iterations
    n_3 = 10**7 #trial 3 iterations
    '''

    #built-in collections table
    #list
    List_1 = [i for i in range(n_1)] #creating lists to search; lists of ints
    List_2 = [i for i in range(n_2)]
    List_3 = [i for i in range(n_3)]

    #parameters of the function for searching a value in a list; each trial
    param_List_1 = (List_1, -1) #searching for "-1" which is not in the list
    param_List_2 = (List_2, -1)
    param_List_3 = (List_3, -1)

    ListC_1 = time_f(search_list, param_List_1) #searching for '-1' as it is not in any of the lists; worst case scenario
    ListC_2 = time_f(search_list, param_List_2) 
    ListC_3 = time_f(search_list, param_List_3)

    #formating the list times into str for printing in the table
    listtime_1 = ("{:.3g} ms".format(ListC_1*1000))
    listtime_2 = ("{:.3g} ms".format(ListC_2*1000))
    listtime_3 = ("{:.3g} ms".format(ListC_3*1000))

    #tuple
    tup_1 = (i for i in range(n_1)) #tuple of ints in ascending order
    tup_2 = (i for i in range(n_2))
    tup_3 = (i for i in range(n_3))

    #parameters of the function for searching a value in a tuple; each trial
    param_tuple_1 = (tup_1, -1) #searching for "-1" which is not in the tuple
    param_tuple_2 = (tup_2, -1)
    param_tuple_3 = (tup_3, -1)

    tupC_1 = time_f(search_Tuple, param_tuple_1) #searching for '-1' as it is not in any of the lists; worst case scenario
    tupC_2 = time_f(search_Tuple, param_tuple_2)
    tupC_3 = time_f(search_Tuple, param_tuple_3)

    #formating the tuple times into str for printing in the table
    tuptime_1 = ("{:.3g} ms".format(tupC_1*1000))
    tuptime_2 = ("{:.3g} ms".format(tupC_2*1000))
    tuptime_3 = ("{:.3g} ms".format(tupC_3*1000))

    #string
    #defining the string with "a"'s with length n
    string_1 = ""
    for i in range(n_1):
        string_1 += "a"

    string_2 = ""
    for i in range(n_2):
        string_2 += "a"

    string_3 = ""
    for i in range(n_3):
        string_3 += "a"

    #parameters of the function for searching a value in a string; each trial
    param_str_1 = (string_1, "z") #searching for "z" which is not in the string
    param_str_2 = (string_2, "z")
    param_str_3 = (string_3, "z")

    strC_1 = time_f(search_str, param_str_1)
    strC_2 = time_f(search_str, param_str_2)
    strC_3 = time_f(search_str, param_str_3)

    #formating the str search times into str for printing in the table
    strtime_1  = ("{:.3g} ms".format(strC_1*1000))
    strtime_2  = ("{:.3g} ms".format(strC_2*1000))
    strtime_3  = ("{:.3g} ms".format(strC_3*1000))

    #set
    #defining 3 sets, with values of a n times
    set_1 = set()
    for i in range(n_1):
        set_1.add("a")

    set_2 = set()
    for i in range(n_2):
        set_2.add("a")
            
    set_3 = set()
    for i in range(n_3):
        set_3.add("a")

    #parameters of the function for searching a value in a set; each trial
    param_set_1 = (set_1, -1) #searching for "-1" which is not in the set
    param_set_2 = (set_2, -1)
    param_set_3 = (set_3, -1)

    #getting the times it takes to search the sets
    setC_1 = time_f(search_set, param_set_1)
    setC_2 = time_f(search_set, param_set_2)
    setC_3 = time_f(search_set, param_set_3)

    #formating the set times into str for printing in the table
    settime_1  = ("{:.3g} ms".format(setC_1*1000))
    settime_2  = ("{:.3g} ms".format(setC_2*1000))
    settime_3  = ("{:.3g} ms".format(setC_3*1000))

    delim = "|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|" #remade according to table length
    line = "|---------------------------------------|" #remade according to table length

    variable_line_collections = "|n\tt_list\tt_tup\tt_str\tt_set\t|"
    collections_1 = str("|" +str(n_1) + "\t" + listtime_1 + "\t" + tuptime_1 + "\t" + strtime_1 + "\t" + settime_1 + "\t|")
    collections_2 = str("|" +str(n_2) + "\t" + listtime_2 + "\t" + tuptime_2 + "\t" + strtime_2 + "\t" + settime_2 + "\t|")
    collections_3 = str("|" +str(n_3) + "\t" + listtime_3 + "\t" + tuptime_3 + "\t" + strtime_3 + "\t" + settime_3 + "\t|")

    #collections table
    print(delim)
    print(variable_line_collections)
    print(line)
    print(collections_1)
    print(collections_2)
    print(collections_3)
    print(delim)
    

