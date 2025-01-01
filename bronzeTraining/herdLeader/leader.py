numCows = int(input())
cows = list(str(input()))
cowRanges = list(map(int,input().split()))
cowsG = []
cowsH = []
for t in range(numCows):
    if cows[t] == "G":
        cowsG.append(t)
    else:
        cowsH.append(t)
cowLocations = [cowsG,cowsH]
switch = 0
if cowLocations[0][0] == 0:
    switch = 1
else:
    switch = 0
secondLeader = cowLocations[switch][0]
if cowRanges[secondLeader]-1 < cowLocations[switch][-1]:
    print(0)
else:
    answer = 0
    for i in cowLocations[switch - 1]:
        if i > secondLeader:
            break
        if cowRanges[i]-1 >= cowLocations[switch - 1][-1] and i == cowLocations[switch - 1][0]:
            answer += 1
            continue
        if cowRanges[i]-1 >= secondLeader:
            answer+=1
    print(answer)