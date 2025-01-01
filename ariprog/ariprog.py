"""
ID:alexand233
LANG: PYTHON3
TASK: ariprog
"""
fin = open("ariprog.in",'r')
fout = open('ariprog.out','w')

import time
start_time = time.time()

bisquareDictionary = {}

def createBisquares(num):
    for t in range(num+1):
        for x in range(t,num+1):
            bisquareDictionary.update({(t**2 + x**2): True})

sequenceLength = int(fin.readline())
limit = int(fin.readline())
maxval = limit**2 * 2
createBisquares(limit)
bisquares = list(bisquareDictionary.keys())
bisquares.sort()
sequences  = []
for t in range(len(bisquares)-sequenceLength+1):
    a = bisquares[t]
    for x in range(t+1,len(bisquares)):
        b = bisquares[x] - a
        final_value = a + b*(sequenceLength-1)
        if (sequenceLength >= 4 and b%4 != 0) or (sequenceLength >= 20 and b%sequenceLength!=0) :
            continue
        if final_value > maxval:
            break
        flag = True
        for y in range(sequenceLength):
            if (a + y*b) not in bisquareDictionary:
                flag = False
                break
        if flag == True:
            sequences.append((b,a))
sequences.sort()
if len(sequences) == 0:
    fout.write("NONE" + "\n")
else:
    for t in range(len(sequences)):
        fout.write(str(sequences[t][1])+" "+str(sequences[t][0])+"\n")
fout.close()

print(time.time() - start_time)