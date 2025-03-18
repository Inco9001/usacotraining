"""
ID:alexand233
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
def createDict(arr):
   final = dict()
   arrFin = []
   for t in range(len(arr)):
       final[t] = arr[t]
       final[tuple(arr[t])] = t 
       arrFin.append(t)
   return final, arrFin


def deepCopy(arr):
  tempArr = []
  for t in arr:
      tempArr.append(t)
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
      minValue = 1000000001
      minValueWormHole = []
      for t in tempMatrix:
          if t[1] < minValue:
              minValue = t[1]
              minValueWormHole = deepCopy(t)
      answer.append(minValueWormHole)
      print(str(tempMatrix) +"to be removed " +  str(minValueWormHole))
      tempMatrix.remove(minValueWormHole)
  return answer

def makeDictForPairings(arr): #Array<Array<Int>>
   ans = dict()
   for t in arr:
      ans.update({t[0]:t[1]})
      ans.update({t[1]:t[0]})
   return ans #Dictionary 

def generateAllParings(arr): 
  if len(arr) > 2:
      finalArr = []
      anchor = arr[0]
      arr.pop(0)
      for t in range(len(arr)):
          recursiveArr = deepCopy(arr) 
          recursiveArr.remove(arr[t]) 
          for i in generateAllParings(recursiveArr): 
            sets = [[anchor,arr[t]]]
            for j in i:
                sets.append(j) 
            finalArr.append(sets)
      return finalArr
  return [[deepCopy(arr)]] 


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
          answer.update({arrOfLevels[i][t+1]:arrOfLevels[i][t]})
      i += 1
  return answer

def findLoops(arr,matrix,outcomes,dictionary):
  connections = makeDictForPairings(matrix)
  for t in arr:
     start = t
     for i in range(len(arr)+1):
        if outcomes[tuple(dictionary[connections[start]])] == "null":
            break
        if i == len(arr):
            return 1
        start = dictionary[outcomes[tuple(dictionary[connections[start]])]] 
  return 0

num_wormholes = int(fin.readline().strip())
arrayOfWormholes = []
for t in range(num_wormholes):
  temp_arr = tuple(map(int,fin.readline().strip().split()))
  arrayOfWormholes.append(temp_arr)
arrayOfWormholes.sort()
arrayOfWormholes = rangeSort(arrayOfWormholes)
outcomes = generateOutcomes(arrayOfWormholes)
reference,listOfReferences = createDict(arrayOfWormholes)
arrOfPossibleWormholePairs = generateAllParings(deepCopy(listOfReferences))
finalAnswer = 0
for t in arrOfPossibleWormholePairs:
   finalAnswer += findLoops(listOfReferences,t,outcomes,reference)
fout.write(str(finalAnswer) + '\n')
