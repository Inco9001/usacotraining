fin = open("mooing2.in","r")
lenString = int(fin.readline())
string = list(map(int,fin.readline().split()))

# lenString = int(input())
# string = list(map(int,input().split()))

def makeDictionary():
    numDict = dict()
    for t in range(lenString): 
        if string[t] not in numDict:
            numDict.update({string[t]:1})
            continue
        numDict.update({string[t]:numDict[string[t]]+1})
    return numDict
usedDuplicate = {}
numDict = makeDictionary()
ans = 0
for t in range(1,lenString+1):
    base = string[-t]
    usedDict = {base:0}
    if base in usedDuplicate or numDict[base] < 2:
        continue
    endpoint = 0
    for x in range(t+1,lenString+1):
        if base == string[-x]:
            endpoint = x
    for x in range(endpoint,lenString+1):
        if string[-x] not in usedDict:
            usedDict.update({string[-x]:0})
            ans += 1
    usedDuplicate.update({base:0})
print(ans)















# string.sort()
# print(string)
# uniqueNumbersList = [string[0]]
# duplicatesList = [0]
# uniqueNumbers = 0
# duplicates = 0
# for t in range(1,lenString):
#     if string[t] == uniqueNumbersList[uniqueNumbers]:
#         if string[t] == duplicatesList[duplicates]:
#             continue
#         duplicatesList.append(string[t])
#         duplicates += 1
#         continue
#     uniqueNumbersList.append(string[t])
#     uniqueNumbers += 1
# print((duplicates*(uniqueNumbers+1))-duplicates)