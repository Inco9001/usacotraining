def createStalls():
    arr = []
    for t in range(100):
        arr.append(0)
    return arr

def toBase2(t,bottomline):
    num = t
    arr = []
    i = 0
    while i != bottomline:
        i += 1
        if num%2 == 1:
            arr.insert(0,1)
            num -= 1
            num = num//2
            continue
        arr.insert(0,0)
        num = num//2
    return arr

#fin = open('/home/eqn/Documents/usacotraining/bronzeTraining/cooling//cooling.in','r')
numCows,numConditioners = map(int,input().split())
coolingRec = dict()
stallKeys = []
for t in range(numCows):
    start,end,cooling = map(int,input().split())
    for x in range(start-1,end):
        stallKeys.append(x)
        coolingRec.update({x:cooling})
airConditioners = []
for t in range(numConditioners):
    airConditioners.append(list(map(int,input().split())))
costs = []
for t in range(2**numConditioners):
    stalls = createStalls()
    config = toBase2(t,numConditioners)
    ans = 0
    flag = True
    for x in range(numConditioners):

        if config[x] != 0:
            ans += airConditioners[x][3]
            for i in range(airConditioners[x][0]-1,airConditioners[x][1]):
                stalls[i] += airConditioners[x][2]
    for x in stallKeys:
        if stalls[x] < coolingRec[x]:
            flag = False
            break
    if flag == True:
        costs.append(ans)
print(min(costs))



