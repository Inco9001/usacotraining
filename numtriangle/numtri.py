"""
ID:alexand233
LANG: PYTHON3
TASK: numtri
"""
fin = open("numtri.in",'r')
fout = open('numtri.out','w')

def generateBestPath(path, oldPath):
    for x in path:
        print(oldPath)
        oldPath.append(x[0]+oldPath[0])
        for t in range(1,len(x)-1):
            oldPath.append(x[t]+max(oldPath[1],oldPath[0]))
            oldPath.pop(0)
        
        oldPath.append(x[-1]+oldPath[0])
        oldPath.pop(0)
    return max(oldPath)

numtriangleLayers = int(fin.readline())
triangleLayers = []
path = []
for t in range(numtriangleLayers):
    if t == 0: 
        path.append(int(fin.readline()))
        continue
    triangleLayers.append(list(map(int,fin.readline().split())))
fout.write(str(generateBestPath(triangleLayers,path)) + "\n")
fout.close()
