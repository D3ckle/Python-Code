# Login.py


import hashlib
import sys


def Login(inputUser, inPassword):
    gangHashedPWsfile = open("../.loginCheck", "r")
    gang=[]
    hashed= {}


    for row in gangHashedPWsfile:
        (user,hashedPW)=(row.strip('\n')).split(',')
        hashed[user]= hashedPW
        gang.append(user)
       
    if inputUser not in gang:
        print('User not found')
        return 0


    hash=hashlib.sha256()
    hash.update(bytes(inputUser+inPassword,'utf-8'))  # for defenses against dictionary attack on the gangHashedPWs file
    for i in range(90000): hash.update(hash.digest())   # prepend name and iterate
    guess=hash.hexdigest()


    if (guess) == hashed[inputUser]:
        return True
        # print('Login successful.')
    else:
        return False
        # print('Login failed: incorrect password.')