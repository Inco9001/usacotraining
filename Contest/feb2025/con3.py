fin = open("con.in","r")
testCases = int(fin.readline())
for t in range(testCases):
    lenArr,numRep = map(int,fin.readline().strip().split())
    numArr = list(map(int,fin.readline().strip().split()))
    condensed = []
    var = numArr[0]
    tempArr = [numArr[0],1]
    for i in range(1,lenArr):
        if numArr[i] == var:
            tempArr[1] += 1
        else:
            condensed.append([tempArr[0],tempArr[1]])
            tempArr = [numArr[i],1]
            var = numArr[i]
    condensed.append([tempArr[0],tempArr[1]])   
    if numRep >= len(condensed):
        print("YES")
        continue
    repeat1 = []
    rep = [numArr[0]]
    for i in range(1,lenArr):
        if rep != repeat1 and len(rep) > len(repeat1):
            for j in rep:
                repeat1.append(j)
            rep = []
            continue
        rep.append(numArr[i])
    print(repeat1)
    conRepeat1 = []
    var = 4
    tempArr = []
    tempArr = [numArr[0],1]
    for i in range(1,lenArr):
        if numArr[i] == var:
            tempArr[1] += 1
        else:
            conRepeat1.append([tempArr[0],tempArr[1]])
            tempArr = [numArr[i],1]
            var = numArr[i]
    conRepeat1.append([tempArr[0],tempArr[1]])   
    if len(conRepeat1) <= numRep:
        print("YES")
    else:
        print("NO")            
