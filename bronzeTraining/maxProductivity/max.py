
# fin = open("max.in","r")
canVisit = dict()
wakeUpTime = dict()

numFarms,numFarmsVisit = map(int,input().strip().split())
farmsClose = list(map(int,input().strip().split()))
timeVisit = list(map(int,input().strip().split()))

def binarySearch(arr, alarmTime):
    low = 0
    high = len(arr)-1
    mid = 0
    while high > low:
        mid = (high+low)//2
        if arr[mid] == alarmTime:
            return canVisit[arr[mid]]
        if arr[mid] < alarmTime:
            high = mid - 1
        else:
            low = mid + 1
    if low == 0:
        if arr[low] < alarmTime:
            return 0
    if arr[low] < alarmTime:
        return canVisit[arr[low-1]]
    return canVisit[arr[high]]                                                           

for t in range(numFarms):
    var = farmsClose[t]-timeVisit[t]-1
    if var in wakeUpTime:

        wakeUpTime.update({var:wakeUpTime[var]+1})
        continue
    if var < 0:
        continue
    wakeUpTime.update({var:1})
oldKey = max(wakeUpTime.keys())
canVisit.update({oldKey:wakeUpTime[oldKey]})
wakeUpTime.pop(oldKey)
keys = [oldKey]
for i in sorted(wakeUpTime.keys(),reverse = True):
    canVisit.update({i:canVisit[oldKey]+wakeUpTime[i]})
    oldKey = i
    keys.append(oldKey)

for t in range(numFarmsVisit):
    numVisits, alarmTime = map(int,input().split())
    if binarySearch(keys,alarmTime) < numVisits:
        print("NO")
    else:
        print("YES")