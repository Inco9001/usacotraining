fin = open("fenceplan.in",'r')
fout = open("fenceplan.out",'w')
numCows, numConnections = map(int,fin.readline().split())
cows = [0]
connections = [0]
cowsNum = [True]+[False]*numCows
best = 2000000000
used = [True]+[False]*numCows
for t in range(numCows):
    cows.append(list(map(int,fin.readline().split())))
    connections.append([])

for t in range(numConnections):
    a,b = map(int,fin.readline().split())
    connections[a].append(b)
    connections[b].append(a)

for t in range(1,numCows+1):
    if cowsNum[t] == True:
        continue
    queu = [1,t]
    queuLen = 1
    used[t] = True
    maxX = cows[queu[1]][0]
    maxY = cows[queu[1]][1]
    minX = cows[queu[1]][0]
    minY = cows[queu[1]][1]
    while queu[0] > 0:
        for j in connections[queu[1]]:
            if used[j] == True:
                continue
            cowsNum[j] = True
            used[j] = True
            queu.append(j)
            queuLen += 1
        maxX = max(cows[queu[1]][0],maxX)
        minX = min(cows[queu[1]][0],minX)
        maxY = max(cows[queu[1]][1],maxY)
        minY = min(cows[queu[1]][1],minY)
        queu.pop(1)
        queuLen -= 1
        queu[0] = queuLen
    if (maxX+maxY-minY-minX)*2 < best:
        best = (maxX+maxY-minY-minX)*2
fout.write(str(best)+"\n")







        
        