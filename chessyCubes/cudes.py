def createDictionary(num):
    dictionary = dict()
    for x in range(3):
        for y in range(num):
            for z in range(num):
                dictionary.update({tuple((x,y,z)):0})
    return dictionary

dimension,cutCubes = map(int,input().split())
dictionary = createDictionary(dimension)
ans = 0
for t in range(cutCubes):
    cutPoint = list(map(int,input().split()))
    Xline = tuple((0,cutPoint[1],cutPoint[2]))
    Yline = tuple((1,cutPoint[0],cutPoint[2]))
    Zline = tuple((2,cutPoint[0],cutPoint[1]))
    dictionary.update({Xline: dictionary[Xline] + 1})
    dictionary.update({Yline: dictionary[Yline] + 1})
    dictionary.update({Zline: dictionary[Zline] + 1})
    if dictionary[Xline] >= dimension:
        ans += 1
    if dictionary[Yline] >= dimension:
        ans += 1
    if dictionary[Zline] >= dimension:
        ans += 1
    print(ans) 
       