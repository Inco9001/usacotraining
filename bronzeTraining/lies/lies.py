#fin = open("lies.in",'r')
numCows = int(input())
lessThan = []
greaterThan = []
for t in range(numCows):
    direction, num = map(str,input().split())
    if direction == "G":
        greaterThan.append(int(num))
    else:
        lessThan.append(int(num))

lessThan.sort()
greaterThan.sort()
numG = len(greaterThan)
numL = len(lessThan)
liars = numCows
lPointer = 0
gPointer = 0
while lPointer < numL and gPointer < numG: 
    lyingCows = 0
    if lessThan[lPointer] < greaterThan[gPointer]:
        lyingCows = lPointer + (numG-gPointer)
        lPointer += 1
    else:
        gPointer += 1
        lyingCows = lPointer + (numG-gPointer)
    if lyingCows < liars:
        liars = lyingCows
i = 1
if lPointer < numL:
    var = numL-lPointer
    while i < var:
        if lPointer + (numG-gPointer) < liars:
            liars = lPointer + (numG-gPointer)
        lPointer += 1
        i += 1
else:
    var = numG-gPointer
    while i < var:
        gPointer += 1
        if lPointer + (numG-gPointer) < liars:
            liars = lPointer + (numG-gPointer)
        i += 1

print(liars)
        