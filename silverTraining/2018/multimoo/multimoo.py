fin = open("multimoo.in","r")
fout = open("multimoo.out","w")

sizeOfCanvas = int(fin.readline())
canvas = []
binaryMatrix = [[0]*sizeOfCanvas]*sizeOfCanvas
for t in range(sizeOfCanvas):
    canvas.append(list(map(int,fin.readline().split())))
for i in range(sizeOfCanvas):
    for j in range(sizeOfCanvas):
        why = "pain"