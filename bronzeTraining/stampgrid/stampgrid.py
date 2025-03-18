cases = int(input())

def deepCopy(matrix):
    newmatrix = []
    for i in range(len(matrix)):
        newline = []
        for j in range(len(matrix[i])):
            newline.append(matrix[i][j])
        newmatrix.append(newline)
    return newmatrix

def rotateStamp(stamp):
    length = len(stamp)
    newStamp = []
    for i in range(length):
        newline = []
        for j in range(length):
            newline.append(0)
        newStamp.append(newline)

    for i in range(length):
        for j in range(length):
            character = stamp[length-j-1][i]
            newStamp[i][j] = character 
    return newStamp

def canApply(canvas, stamp, i, j):
    if i + len(stamp) -1 >= len(canvas) or j + len(stamp) - 1 >= len(canvas):
        return False
    for a in range(len(stamp)):
        for b in range(len(stamp)):
            if canvas[i+a][j+b] == '.' and stamp[a][b] == '*':
                return False
    
    # print(canvas, stamp, i, j)
    return True

def apply(canvas, stamp, i, j):
    for a in range(len(stamp)):
        for b in range(len(stamp)):
            if stamp[a][b] == '*':
                canvas[i+a][j+b] = '.'

for i in range(cases):
    input() # burn new line delimiter
    canvassize = int(input())
    targetcanvas = []
    for j in range(canvassize):
        targetcanvas.append(list(input().strip()))
    stampsize = int(input())
    stamp = []
    for j in range(stampsize):
        stamp.append(list(input().strip()))

    # Get all stamp rotations    
    allStamps = []
    allStamps.append(stamp)
    allStamps.append(rotateStamp(allStamps[0]))
    allStamps.append(rotateStamp(allStamps[1]))
    allStamps.append(rotateStamp(allStamps[2]))

    # if i == 0:
    #     print(allStamps)

    checkmatrix = deepCopy(targetcanvas)

    for a in range(canvassize - stampsize + 1):
        for b in range(canvassize - stampsize + 1):
            for c in range(len(allStamps)):
                if canApply(targetcanvas, allStamps[c], a, b):
                    apply(checkmatrix, allStamps[c], a, b)

    paintable = True
    for a in range(canvassize):
        for b in range(canvassize):
            if checkmatrix[a][b] == '*':
                paintable = False

    if paintable:
        print("YES")
    else:
        print("NO")
        