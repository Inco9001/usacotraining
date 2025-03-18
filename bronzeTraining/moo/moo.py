
numString = int(input())
for t in range(numString):
    search = []
    findMoo = list(str(input()))
    for t in range(len(findMoo)-2):
        if findMoo[t] == "M" and findMoo[t+1] == "O" and findMoo[t+2] == "O":
            search.append(0)
            break
        if findMoo[t] == "M" and findMoo[t+1] == "O" and findMoo[t+2] == "M":
            search.append(1)
        if findMoo[t] == "O" and findMoo[t+1] == "O" and findMoo[t+2] == "M":
            search.append(2)
        if findMoo[t] == "O" and findMoo[t+1] == "O" and findMoo[t+2] == "O":
            search.append(1)
    if len(search) == 0:
        print(-1)
        continue
    print(min(search)+len(findMoo)-3)