class Task:
    """ a task for the operating system to complete."""
    def __init__(self, id, cycles_left):
        self.id = id #a unique identifier (an int)
        self.cycles_left = cycles_left #the amount of cycles necessary to complete this task
        self.prev = self #by default, a single task should point to itself since it is by itself a circle
        self.next = self

    def reduce_cycles(self, num=1):
       '''reduces cycles_left by the appropriate amount'''
       if (self.cycles_left - num < 0): #making anytihng lower than 0, equal to 0 since it'll be removed anyways
           self.cycles_left = 0
       else:
           self.cycles_left -= num #reduce the cycles by than number
       '''If a task is reduced to 0 cycles by reduce_cycles, then the TaskQueue should remove that task from
       the queue and print out info - the task id and the total numebr of clock cycles executed before it finished
       (see Examples below for formatting)'''

       

class TaskQueue:
    """A circular data structure with attributes"""
    
    def __init__(self, cycles_per_task = 1):
        self.current = None #the current task to process
        self.cycles_per_task = cycles_per_task # the amount of cycles to be done after each clock cycle
        self.dict = {} #makes grabbing info easier, and is_empty and len() to have O(1)

    def add_task(self, task):
        ''' adds a task immediately before current. This means it will be the last task to
        be processed. Should be O(1).'''
        #if there is nothing in the TaskQueue yet
        if (self.current == None):
            self.current = task #make the task to be added be the current task in the queue
            #current will not change unless the current is removed
        
        #since it's a circular data structure, it must be able to loop around to other tasks once added.
        #adding the second task in the queue
        elif((not self.current == None) & (self.current.prev == None)):#if there is already one task in the queue
            task.next = self.current #prepare the link, so that the task knows the current is the next task
            self.current.prev = task #add the task to "prev" of the current task
            #to make queue a circle
            self.current.next = task #loops around
        #2 or more tasks, adding a 3rd, means the "ends" must connect to each other
        else: #is there a task before the current

            #now I can link the new task to look to the current and old prev
            task.next = self.current #assign the task's next link to the current
            task.prev = self.current.prev #assign the current's prev link to the task newly added becasue the task will be in between
            
            #must modify the old prev and the links to it to add the new task between the current and old prev
            self.current.prev.next = task #modifying the prev's links
            self.current.prev = task 
            #since the current is default to the first added task, and all tasks added from here are before the current,
            #so i dont have to worry about modifying the tasks that proceed the current  

        #adding to a dictonary to make grabbing specific info easier, and make the len and is_empty more efficent
        self.dict.update({task.id: task}) #having a dictionary makes len and is_empty much easier and operate in O(1)

        #since this added task is added befroe the current, the "next" is current, and previous is nothing:
        #must redefine the old current to have the prev be this newly added task
        

    def remove_task(self, del_id):
        '''removes the task with a given id. O(n) is fine, but you can get this to O(1) if
        you're clever'''
        try:
            #remove the task by having the tasks before and after it point to each other    
            self.dict[del_id].prev.next = self.dict[del_id].next #previous task will be assigned to the next task, bypassing the task to be deleted
            self.dict[del_id].next.prev = self.dict[del_id].prev #next task will be assigned to the previous task, bypassing the task to be deleted

            if(self.dict[del_id] == self.current): #if trying to remove the current task
                if (len(self) == 1): #if the task being deleted is the only task left
                    #so when you delete the only value in the queue, the queue is empty now
                    self.current = None
                else: 
                    self.current = self.current.next #shift the current index to the next Task

            self.dict.pop(del_id) #remove from the dictionary too

        except:
            raise RuntimeError("id " + str(del_id) + " not in TaskQueue") #raises an error if the task id is not in the taskQueue
        '''If a user tries to remove a task with an id that is not in the TaskQueue, you should raise a RuntimeError
        with an appropriate string.
        This check should run in O(1). Think - what data structure can you use that allows O(1)
        membership testing?
        Test this behavior. (The error, not the running time)'''

    def __len__(self): 
        '''len - the number of tasks in the TaskQueue. O(1).'''
        return len(self.dict) #i have a len variable that keeps track of the number of tasks in the queue, so i return that when i want length

    def is_empty(self):
        '''returns True if the TaskQueue is empty; false otherwise. O(1).'''
        return not any(self.dict) #no matter the length of the taskQueue, the current should have a node of some sort unless there is no task in the queue
        ''' Boolean functions like is_empty should have tests for True and False scenarios (self.assertTrue()
        and self.assertFalse())'''

    def execute_tasks(self):
        '''executes tasks cyclically until all tasks are exhuasted'''
        current_ID = self.current.id #int to keep track with task is currently being called
        total = 0 #to be returned at end; total number of cycles it took to execute all tasks.
        while not self.is_empty(): #goes for the number of clock cycles remaining,will complete and remove all tasks in the taskQueue
            
            #which is until all tasks have been executed, reduced cycles_left for each task to 0, and removed
            #Each task will run for cycles_per_task or the amount of clock cycles 
            #it has remaining, whichever is lower.
            #total +=1 #add to cycles since starting a new cycle

            if (self.dict[current_ID].cycles_left >= self.cycles_per_task): #if there is more cycles in the task than what will be subtracted by completing the clock cycle
                self.dict[current_ID].reduce_cycles(self.cycles_per_task) #reduces cycles for the specific task by the amount specified
                current_ID = self.dict[current_ID].next.id #prepare for next clock cycle by moving onto next task
                total+=self.cycles_per_task #add to the cycles since it eas able to complete the cycle
            else: #task.cycle_left < cycle_per_task
                total+=self.dict[current_ID].cycles_left #add the remaining cycles_left to the total
                self.dict[current_ID].reduce_cycles(self.dict[current_ID].cycles_left) #reducing the task's cycles to 0, and prompting to remove the task since it is finished
                #since we now completed the task, it should print out its info and be removed
                print("Finished task", current_ID, "after", total, "clock cycles") #printing the info of the task and how long it took to complete
                temp = current_ID #temp needed because we are deleting the other temp, and since it is needed to get the next task in the circle, we need a temp
                current_ID = self.dict[current_ID].next.id #defining the other temp variable to keep going
                self.remove_task(temp) #we remove the task

        return total #return the total number of cycles it took to execute all tasks.
    #start at current, using its 'next' for second cycle