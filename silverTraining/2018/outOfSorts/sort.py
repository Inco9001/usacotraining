fin = open("sort.in","r")
fout = open("sort.out",'w')

numNum = int(fin.readline())
sortedArr = []
sortedDict = dict()
unSortedArr = []
maxDistance = 0
for t in range(1,numNum+1):
    element = int(fin.readline())
    sortedArr.append(element)
    unSortedArr.append(element)
    sortedDict.update({element:0})
sortedArr.sort()
for t in range(numNum):
    sortedDict[sortedArr[t]] = t
for t in range(numNum):
    if t-sortedDict[unSortedArr[t]] > maxDistance:
        maxDistance = t-sortedDict[unSortedArr[t]]

fout.write(str(maxDistance+1)+"\n")
print(maxDistance+1)
