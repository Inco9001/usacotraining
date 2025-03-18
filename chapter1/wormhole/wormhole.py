"""
ID:alexand233
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
def deepCopy(arr):
    tempArr = []
    for t in range(len(arr)):
        tempArr.append(arr[t])
    return tempArr

def matrixDeepCopy(matrix):
    answer = []
    for t in matrix:
        answer.append(deepCopy(t))
    return answer 

def rangeSort(matrix):
    answer = []
    tempMatrix = matrixDeepCopy(matrix)
    while len(tempMatrix) > 0:
        minValue = 1000001
        minValueWormHole = []
        for t in tempMatrix:
            if t[1] < minValue:
                minValue = t[1]
                minValueWormHole = deepCopy(t)
        answer.append(minValueWormHole)
        tempMatrix.remove(minValueWormHole)
    return answer

def matrixDeepCopy(arr):
    finalArr = []
    for t in range(len(arr)):
        tempArr = []
        for x in range(2):
            tempArr.append(arr[t][x])
        finalArr.append(deepCopy(tempArr))
    return finalArr

def generateAllParings(arr):
    if len(arr) > 2:
        finalArr = []
        anchorArr = [arr[0]]
        arr.pop(0)
        for t in arr:
            setOfPairsArr = []
            recursiveArr = deepCopy(arr)
            anchorArr.append(t)
            recursiveArr.remove(t)
            setOfPairsArr.append(deepCopy(anchorArr))
            setOfPairsArr.append(generateAllParings(recursiveArr))
            finalArr.append(setOfPairsArr)
            anchorArr.remove(t)
        return finalArr
    return deepCopy(arr)

def generateOutcomes(arr):
    answer = dict()
    arrOfLevels = []
    temp_arr = []
    for t in arr:
        if len(temp_arr) == 0:
            temp_arr.append(tuple(deepCopy(t)))
            continue
        if t[1] == temp_arr[0][1]:
            temp_arr.append(tuple(deepCopy(t)))
            continue
        arrOfLevels.append(tuple(deepCopy(temp_arr)))
        temp_arr = [tuple(deepCopy(t))]
    if len(temp_arr) != 0:
        arrOfLevels.append(tuple(deepCopy(temp_arr)))
    i = 0
    while i < len(arrOfLevels):
        r = len(arrOfLevels[i])
        for t in range(r):
            if t+1 == r:
                answer.update({arrOfLevels[i][t]:"null"})
                break
            answer.update({arrOfLevels[i][t]:arrOfLevels[i][t+1]})
        i += 1
    return answer

def findLoops(arr,matrix,dictionary):
    ans = 0
    for t in arr:
        wormhole
        for i in range(len(matrix)+1):
            print()
    return ans

num_wormholes = int(fin.readline().strip())
arrayOfWormholes = []
for t in range(num_wormholes):
    temp_arr = tuple(map(int,fin.readline().strip().split()))
    arrayOfWormholes.append(temp_arr)
arrayOfWormholes.sort()
arrayOfWormholes = rangeSort(arrayOfWormholes)
outcomes = generateOutcomes(arrayOfWormholes)
arrOfPossibleWormholePairs = generateAllParings(arrayOfWormholes)  
arrayOfWormholes.append(deepCopy(arrOfPossibleWormholePairs[0][0][0]))
finalAnswer = 0
for t in arrOfPossibleWormholePairs:
    print(t)
    finalAnswer += findLoops(arrayOfWormholes,arrOfPossibleWormholePairs,outcomes)
fout.write(str(finalAnswer) + '\n')


