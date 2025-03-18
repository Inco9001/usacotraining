"""
ID:alexand233
LANG: PYTHON3
TASK: sprime
"""
fin = open("sprime.in",'r')
fout = open('sprime.out','w')
ribs = int(fin.readline())
import math

def isPrime(num):
    flag = True
    t = 2
    while t <= math.sqrt(num):
        if num%t == 0:
            flag = False
            break
        t += 1
    return flag

def generateSuperPrimes(num):
    queue = ['2','3','5','7']
    while len(list(queue[0])) < num:
        for t in range(1,10,2):
            if isPrime(int(queue[0] + str(t))):
                queue.append(queue[0] + str(t))
        queue.pop(0)
    for t in queue:
        fout.write(str(t)+"\n")

generateSuperPrimes(ribs)
fout.close