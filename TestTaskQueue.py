from audioop import add
from TaskQueue import Task, TaskQueue
import unittest

class TestTaskQueue(unittest.TestCase):

    def test_init(self): 
        #init Task tests
        task1 = Task(1, 3) #task with ID = 1, cycles_left = 3, and defualt prev and next links both = None
        self.assertEqual(task1.id, 1) #check id
        self.assertEqual(task1.cycles_left, 3) #check cycles left
        self.assertEqual(task1.prev, task1) #not attached to another node behind, so it points to itself since there is no end
        self.assertEqual(task1.next, task1) #not attached to another node in front, so it points to itself

        task2 = Task(2, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task2.cycles_left, 1)
        self.assertEqual(task2.prev, task2)
        self.assertEqual(task2.next, task2)

        #init TaskQueue tests
        TQ = TaskQueue()  #cycles = 1
        self.assertEqual(TQ.current, None)
        self.assertEqual(TQ.cycles_per_task, 1) #default is 1
        self.assertEqual(len(TQ), 0) #always will be 0 at initialization

        TQ2 = TaskQueue(10)
        self.assertEqual(TQ2.current, None)
        self.assertEqual(TQ2.cycles_per_task, 10) #made to be 10 from defining 2 lines before
        self.assertEqual(len(TQ), 0) #always will be 0 at initialization

    def test_reduce_cycles(self):
        task1 = Task(1, 3)
        self.assertEqual(task1.cycles_left, 3)
        task1.reduce_cycles() #reduced by 1
        self.assertEqual(task1.cycles_left, 2) #3 - 1 = 2
        task1.reduce_cycles(2) #reduced by 1
        self.assertEqual(task1.cycles_left, 0) #2 - 2 = 0
        task2 = Task(2, 5)
        #in taskQueue
        TQ = TaskQueue()
        TQ.add_task(task2)
        TQ.current.reduce_cycles(3)
        self.assertEqual(TQ.current.cycles_left, 2)

    def test_add_task(self): 
        task1 = Task(1, 3)
        task2 = Task(2, 1)
        task3 = Task(3, 2)
        TQ = TaskQueue()
        list_tasks = [task1, task2, task3] #creating a list to make adding to the taskqueue easier
        for tasks in list_tasks: #should be (from left to right) task2, task3, task1; task1 being current
            TQ.add_task(tasks)

        #current should still be task1 since it was first added and doesnt change unless removed
        self.assertEqual(TQ.current, task1) #the very first added task should be the current
        self.assertEqual(TQ.current.prev, task3) #since task1 is current, and task3 was most recently added
        #task2, it should be current's next's link
        self.assertEqual(TQ.current.next, task2) #current's next should loop around to the second added task, which should be task2
        self.assertEqual(TQ.current.next.id, task2.id) #just checking to make sure further information can be accessed
        self.assertEqual(TQ.current.prev.prev, task2) #current = task1, current.prev = task3, current.prev.prev = task2
        #checks to make sure links are properly created
        self.assertEqual(TQ.current.next.next, task3) #current = task1, current.next = task2, current.next.next = task3
        
    def test_remove_task(self): 
        t1 = Task(1, 3)
        t2 = Task(2, 3)
        TQ = TaskQueue()
        TQ.add_task(t1) #adding tasks to be removed
        TQ.add_task(t2)
        self.assertEqual(len(TQ), 2)

        TQ.remove_task(2) #removing task2

        self.assertEqual(len(TQ), 1) #2 tasks were added, 1 removed, len should be 1
        self.assertEqual(TQ.current, t1)
        self.assertEqual(TQ.current.next, t1)
        self.assertEqual(TQ.current.prev, t1)
        self.assertEqual(TQ.current.id, 1)
        self.assertEqual(len(TQ), 1)
        
        TQ.remove_task(1) #removing the last task in the Queue, 
        #len should be 0 and there shouldnt be a current anymore since there is no task
        self.assertEqual(len(TQ), 0)
        self.assertEqual(TQ.current, None)

    def test_len(self): 
        task1 = Task(1, 2)
        task2 = Task(2, 3)
        task3 = Task(3, 4)

        list_of_tasks = [task1, task2, task3]
        TQ = TaskQueue()
        self.assertEqual(len(TQ), 0) #nothing has been added yet, so length should be 0
        for i in list_of_tasks:
            TQ.add_task(i)
        self.assertEqual(len(TQ), 3) #a total of 3 tasks have been added, so length should be 3
        
        #TQ.remove_task(4) #there is no task 4 so length shouldnt change; still 3
        #self.assertEqual(len(TQ), 3)

        TQ.remove_task(3) #task3 should have been removed
        self.assertEqual(len(TQ), 2)
        

    def test_is_empty(self): 
        t1 = Task(1, 3)
        TQ = TaskQueue()
        self.assertTrue(TQ.is_empty()) #no added taskes yet, only just defined, expected false
        
        TQ.add_task(t1) #adding a task; there is something in the taskqueue now
        self.assertFalse(TQ.is_empty()) #task is added, so at the very least there is a task inside; expected true


    def test_execute_tasks(self): 

        t1 = Task(1, 3) #task 1 with 3 cycles left
        t2 = Task(2, 1) #task 2 with 1 cycles left
        t3 = Task(3, 5) #task 3 with 5 cycles left
        l_task = [t1, t2, t3]
        TQ = TaskQueue()
        for i in l_task:
            TQ.add_task(i)
            
        t_total = TQ.execute_tasks()
        self.assertEqual(t_total, 9)
        #t1 = 3>>2>>1>>0, print 6
        #t2 = 1>>0, print 2
        #t3 = 5>>4>>3>>2>>1>>0, print 9, total clock cycles
        print(f"cycles = {t_total}")
        self.assertEqual(len(TQ), 0)

        t1 = Task(1, 3)
        t2 = Task(2, 5)
        l_task = [t1, t2]
        for i in l_task:
            TQ.add_task(i)
        
        t_total = TQ.execute_tasks()
        self.assertEqual(t_total, 8)
        #t1 = 3>>2>>1>>0, print 6
        #t2 = 1>>0, print 2
        #t3 = 5>>4>>3>>2>>1>>0, print 9, total clock cycles
        print(f"cycles = {t_total}")
        self.assertEqual(len(TQ), 0)

        '''
        task1 = Task(1, 8)
        task2 = Task(2, 4)
        task3 = Task(3, 10)
        l_task2 = [task1, task2, task3]
        TQ2 = TaskQueue(2) #reducing by cycles in each task by 2
        for i in l_task2:
            TQ2.add_task(i)
        t_total2 = TQ2.execute_tasks()
        self.assertEqual(t_total2, 11) 
        #task1 start: 8>>6>>4>>2>>0,print(9)
        #task2 start: 4>>2>>0, print(5)
        #task3 start:10>>8>>6>>4>>2>>0, print(11), total 11
        print(f"cycles = {t_total2}")

        t_1 = Task(1,3)
        t_2 = Task(2,4)
        t_3 = Task(3,1)
        t_4 = Task(4,2)
        t_5 = Task(5,5)
        t_list = [t_1,t_2,t_3,t_4,t_5]
        TQ3 = TaskQueue()
        for i in t_list:
            TQ3.add_task(i)
        t_total3 = TQ3.execute_tasks()
        self.assertEqual(t_total3, 15) 
        #task1 start: 3>>2>>1>>0 print10
        #task2 start: 4>>3>>2>>1>>0 print 13
        #task3 start: 1>>0 print3
        #task4 start: 2>>1>>0 print8
        #task5 start: 5>>4>>3>>2>>1>>0 print 15
        print(f"cycles = {t_total3}")
        self.assertEqual(len(TQ3), 0) #since the tasks are removed 

        t1 = Task(1, 3)
        t3 = Task(3, 5)
        TQ4 = TaskQueue(10)
        TQ4.add_task(t1)
        TQ4.add_task(t3)

        t_total4 = TQ4.execute_tasks()
        self.assertEqual(t_total4, 2) # 2 cycles
        #task1 start: 3>>0 pinrt1
        #task3 start: 5>>0 print2
        print(f"cycles = {t_total4}")
        self.assertEqual(len(TQ4), 0) #since the tasks are removed 

        t1 = Task(1, 2)
        TQ5 = TaskQueue(2)
        TQ5.add_task(t1)
        t_total5 = TQ5.execute_tasks()
        print(f"cycles = {t_total5}")
        self.assertEqual(len(TQ5), 0) #since the tasks are removed

        TQ5.add_task(t1)

        #just adding again and seeing if it works
        t_total6 = TQ5.execute_tasks()
        print(f"cycles = {t_total6}")
        self.assertEqual(len(TQ5), 0) #since the tasks are removed

        t1 = Task(1,1)
        t2 = Task(2,1)
        T_Q = TaskQueue(2)

        T_Q.add_task(t1)
        T_Q.add_task(t2)

        time = T_Q.execute_tasks()
        print(f"cycles = {time}")
        self.assertEqual(time, 2)
        self.assertEqual(T_Q.current, None)
        self.assertEqual(len(T_Q), 0) #since the tasks are removed
        '''

if __name__ == '__main__':
    unittest.main()
    '''test the public interface of your class. You do not need to test any private methods or attributes you
create.
Exceptions are part of the public interface: test that your code raises the correct Errors in the correct
circumstances.
Boolean functions like is_empty should have tests for True and False scenarios (self.assertTrue()
and self.assertFalse())'''


'''questions to ask tm

when removing the current task, what should the next 'current' be?
current.next

what are clock_cycles?
number of times to process through entire taskqueue, happens each time reduce_cycles is called

what is the relationship between cycles_left, cycles_per_task, and clock_cycles?

in hw example, order is 2 1 3, but how does that happen if we're only adding BEFORE current, 
is 'current' changing?
my way is correct, HW printing is actually just order of tasks being deleted after execute_tasks method
2341
231
23451 is order
show example with 4 tasks, 5 tasks?

special behavior -  task is reduced to 0 cycles - is that occuring during the execute_tasks()

"executes tasks cyclically until all tasks are exhuasted. Each task will run for cycles_per_task
or the amount of clock cycles it has remaining, whichever is lower. This should print out
information whenever a task is finished (see examples for string formatting). At the end,
return the total number of cycles it took to execute all tasks."








'''

