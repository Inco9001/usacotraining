"""
ID:alexand233
LANG: PYTHON3
TASK: milk3
"""
fin = open("milk3.in",'r')
fout = open('milk3.out','w')
bucketMax = tuple(map(int, fin.readline().split()))
transforms = [
    (0,1),
    (0,2),
    (1,0),
    (1,2),
    (2,0),
    (2,1)
]

def getState(currentState, bucketMax, transform):
    space = bucketMax[transform[1]]-currentState[transform[1]]
    amountPoured = min(currentState[transform[0]], space)
    newState = list(currentState)
    newState[transform[0]] = newState[transform[0]] - amountPoured
    newState[transform[1]] = newState[transform[1]] + amountPoured
    return tuple(newState)

initialState = (0, 0, bucketMax[2])

searchedStates = {initialState}
cValues = set()
queue = [initialState]

while len(queue) != 0:
    currentState = queue.pop(0)
    if currentState[0] == 0:
        cValues.add(currentState[2])

    for i in transforms:
        newState = getState(currentState, bucketMax, i)
        if newState not in searchedStates:
            searchedStates.add(newState)
            queue.append(newState)

validValues = list(cValues)
validValues.sort()

output = ""

for i in validValues:
    output = output + " " + str(i)

fout.write(output.strip() + "\n")

