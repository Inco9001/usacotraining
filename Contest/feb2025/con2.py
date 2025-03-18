# fin = open("con.in","r")
# numNum = int(fin.readline())
# nums = list(map(int,fin.readline().split()))
numNum = int(input())
nums = list(map(int,input().split()))
nums.sort()
dictOfNum = dict()
lastValNum = numNum + 1
numToFind = 0
for x in range(numNum):
    t = nums[x]
    while t > numToFind:
        dictOfNum.update({numToFind:0})
        numToFind += 1
    if t == numToFind:
        numToFind += 1
    if t != lastValNum:
        dictOfNum.update({t:1})
        lastValNum = t
    else:
        dictOfNum.update({t:dictOfNum[t]+1})
while numToFind <= numNum:
    dictOfNum.update({numToFind:0})
    numToFind += 1

arr = list(dictOfNum.keys())
numZero = 0
for t in arr:
    if dictOfNum[t] == 0:
        print(numZero)
        numZero += 1
        continue
    if numZero > dictOfNum[t]:
        print(numZero)
    else:
        print(dictOfNum[t])

