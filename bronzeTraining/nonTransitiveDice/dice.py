def generateNumbers():
    arr = []
    for t in range(1,11):
        for x in range(1,11):
            for y in range(1,11):
                for z in range(1,11):
                    arr.append([t,x,y,z])
    return arr

def diceSetUp(a,b):
    aWins = 0
    bWins = 0
    for t in a:
        for x in b:
            if t > x:
                aWins += 1
            if x > t:
                bWins += 1
    if bWins > aWins:
        
        return False
    return True

def canBeTransitive():
    flag = False
    diceFaces = list(map(int,input().split()))
    a = [diceFaces[0],diceFaces[1],diceFaces[2],diceFaces[3]]
    b = [diceFaces[4],diceFaces[5],diceFaces[6],diceFaces[7]]
    aBeatsB = diceSetUp(a,b)
    possibleDiceFacesForC = generateNumbers()
    for c in possibleDiceFacesForC:
        cWins = [0,0,0,0]
        for x in range(4): 
            for t in range(4):
                if a[t] < c[x]:
                    cWins[0] += 1
                elif a[t] > c[x]:
                    cWins[2] += 1
                if b[t] < c[x]:
                    cWins[1] += 1
                elif b[t] > c[x]:
                    cWins[3] += 1
        if aBeatsB:
            if cWins[0] > cWins[2] and cWins[1] < cWins[3]:
                return True
        else:
            if cWins[1] > cWins[3] and cWins[0] < cWins[2]:
                return True
    return flag

numOfCases = int(input())
for t in range(numOfCases):
    if canBeTransitive():
        print("yes")
    else:
        print("no")