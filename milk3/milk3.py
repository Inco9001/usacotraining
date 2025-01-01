"""
ID:alexand233
LANG: PYTHON3
TASK: milk3
"""
fin = open("milk3.in",'r')
fout = open('milk3.out','w')
bucketAmax, bucketBmax, bucketCmax = map(int,fin.readline().split())
bucketStates = [bucketCmax]
queue = []
bucketStatesDict = dict()
queue.append([0,0,bucketCmax])
while len(queue) > 0:
    bucketA, bucketB, bucketC = map(int,queue[0])
    bucketStatesDict.update({(queue[0][0],queue[0][1],queue[0][2]):True})
    queue.pop(0)
    aCapcity = bucketAmax - bucketA
    bCapcity = bucketBmax - bucketB
    cCapcity = bucketCmax - bucketC
    #bucket C -> a
    if bucketA+bucketC > bucketAmax:
        if (bucketAmax,bucketB,bucketC-aCapcity) not in bucketStatesDict:
            queue.append([bucketAmax,bucketB,bucketC-aCapcity])
    else:
        if (bucketA+bucketC,bucketB,0) not in bucketStatesDict:
            queue.append([bucketA+bucketC,bucketB,0])
    #bucket c -> b
    if bucketB+bucketC > bucketBmax:
        if (bucketA,bucketBmax,bucketC-bCapcity) not in bucketStatesDict:
            queue.append([bucketA,bucketBmax,bucketC-bCapcity])
            if bucketA == 0:
                bucketStates.append(bucketC-bCapcity)
    else:
        if (bucketA,bucketB+bucketC,0) not in bucketStatesDict:
            queue.append([bucketA,bucketB+bucketC,0])
            if bucketA == 0:
                bucketStates.append(0)
    #bucket b -> a
    if bucketA+bucketB > bucketAmax:
        if (bucketAmax,bucketB-aCapcity,bucketC) not in bucketStatesDict:
            queue.append([bucketAmax,bucketB-aCapcity,bucketC])
    else:
        if (bucketA + bucketB, 0, bucketC) not in bucketStatesDict:
            queue.append([bucketA + bucketB, 0, bucketC])
    #bucket b -> c
    if bucketC+bucketB > bucketCmax:
        if (bucketA,bucketB-cCapcity,bucketCmax) not in bucketStatesDict:
            queue.append([bucketA,bucketB-cCapcity,bucketCmax])
    else:
        if (bucketA, 0, bucketC + bucketB) not in bucketStatesDict:
            queue.append([bucketA, 0, bucketC + bucketB])
            if bucketA == 0:
                bucketStates.append(bucketC+bucketB)
    #bucket a -> C
    if bucketC+bucketA > bucketCmax:
        if (bucketA-cCapcity,bucketB,bucketCmax) not in bucketStatesDict:
            queue.append([bucketA-cCapcity,bucketB,bucketCmax])
    else:
        if (0, bucketB, bucketC + bucketA) not in bucketStatesDict:
            queue.append([0, bucketB, bucketC + bucketA])
            bucketStates.append(bucketC+bucketA)
    #bucket a -> b
    if bucketB+bucketA > bucketBmax:
        if (bucketA-bCapcity,bucketBmax,bucketC) not in bucketStatesDict:
            queue.append([bucketA-bCapcity,bucketBmax,bucketC])
    else:
        if (0, bucketB + bucketA, bucketC) not in bucketStatesDict:
            queue.append([0, bucketB + bucketA, bucketC])
            bucketStates.append(bucketC)
bucketStates.sort()
final = ''
for t in range(len(bucketStates)):
    if bucketStates[t] != bucketStates[t-1]:
        final += str(bucketStates[t])
        final += " "
fout.write(final.strip() + "\n")


