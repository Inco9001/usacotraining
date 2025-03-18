fin = open("factory.in",'r')
fout = open("factory.out",'w')
num_stations = int(fin.readline())
graphOfWalkWays = [0]
for t in range(num_stations):
    graphOfWalkWays.append([0])
for t in range(num_stations-1):
    child,parent = map(int,fin.readline().split())
    graphOfWalkWays[parent].append(child)
    graphOfWalkWays[child][0] = parent
i = graphOfWalkWays[1][0]
while graphOfWalkWays[i][0] != 0:
    i = graphOfWalkWays[i][0]
flag = True
queu = [i]
used = dict()
while len(queu) != 0:
    used.update({queu[0]:True})
    for t in graphOfWalkWays[queu[0]]:
       if t in used or t == 0:
           continue
       queu.append(t)
    queu.pop(0)
if len(used) == num_stations:
    fout.write(str(i) + "\n")
else:
    fout.write(str(-1)+"\n") 

