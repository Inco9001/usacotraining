# fin = open("Astral.in",'r')
def deepCopy(arr):
    finArr = []
    for t in arr:
        finArr.append(t)
    return finArr
def solve():
    photo = []
    # photoSize,xShift,yShift = map(int,fin.readline().split())
    photoSize,xShift,yShift = map(int,input().split())
    for t in range(photoSize):
        tempArr = []
        # for x in fin.readline().strip():
        for x in input().strip():
            tempArr.append(x)
        photo.append(deepCopy(tempArr))
    startingStars = 0
    movedStars = []
    numBlackPixels = 0
    validBlackPixels = 0
    for x in range(photoSize):
        for y in range(photoSize):
            if photo[x][y] == "B":
                numBlackPixels += 1
            if photo[x][y] == "G" or photo[x][y] == "B":
                if x+yShift < photoSize and y+xShift < photoSize:
                    if photo[x+yShift][y+xShift] == "G" or photo[x+yShift][y+xShift] == "B":
                        startingStars += 1
                        movedStars.append([x+yShift,y+xShift])
                        if photo[x][y] == "B":
                            if [x,y] in movedStars:
                                validBlackPixels += 1
                        continue
                if photo[x][y] == "B":
                    if [x,y] in movedStars:
                        startingStars += 1
                        validBlackPixels += 1
                    continue
                if [x,y] in movedStars:
                    continue
                startingStars += 1
    if numBlackPixels != validBlackPixels:
        return -1
    return startingStars

# numTestCases = int(fin.readline())
numTestCases = int(input())
for t in range(numTestCases): 
    print(solve())