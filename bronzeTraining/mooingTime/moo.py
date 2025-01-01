
dictionaryOfMoos = {} # Mapping of <moo> -> frequency

def addMoo(moo):
    if moo in dictionaryOfMoos.keys():
        dictionaryOfMoos[moo] = dictionaryOfMoos[moo] + 1
    else:
        dictionaryOfMoos[moo] = 1
    return

def deepCopy(arr):
    temp = []
    for t in arr:
        temp.append(t)
    return temp

def printMoos(arr):
    string = ""
    for t in arr:
        string += t
    print(string)
    return

def uncorruptedMoos(data,lengthOfStrings):
    index = 0 
    listOfMoos = []
    potentialCorruption = []
    while index < lengthOfStrings-2:
        if data[index] != data[index+1] and data[index + 1] == data[index + 2]:
            listOfMoos.append((data[index],data[index+1],data[index+2]))
            index += 1
            continue
        if ((data[index] == data[index+1] and data[index + 1] == data[index + 2]) or 
            (data[index] != data[index+2]) or (data[index] != data[index+1])):
            potentialCorruption.append([data[index],data[index+1],data[index+2]])
        index += 1
    listOfMoos.sort()
    return listOfMoos, potentialCorruption

def isMoo(listOfMoos):
    var = 1
    listOfFrequency = []
    potentialMoos = []
    for t in range(len(listOfMoos)-1):
        if listOfMoos[t] == listOfMoos[t+1]:
            var += 1
            continue
        if frequency <= var:
            listOfFrequency.append(listOfMoos[t])
        if frequency-1 == var:
            potentialMoos.append(listOfMoos[t])
        var = 1
    
    if frequency <= var:
        listOfFrequency.append(listOfMoos[-1])
        return listOfFrequency, potentialMoos
    if frequency-1 <= var:
        potentialMoos.append(listOfMoos[-1])
    return listOfFrequency, potentialMoos

def corruptedMoos(target,arr):
    data = []
    t = 0
    while t < len(arr)-2:
        if arr[t] == target[0] and arr[t+1] == target[1] and arr[t+2] == target[2]:
            data.append("null")
            t += 3
            continue
        data.append(arr[t])
        t += 1
    if arr[-1] != target[0] or arr[-2] != target[1] or arr[-3] != target[2]:
        data.append(arr[-1])
        data.append(arr[-2])
    
    for t in range(len(data)-2):
        if data[t] == "null" or data[t+1] == "null" or data[t+2] == "null":
            continue
        if ((data[t] == target[0] and data[t+1] == target[1]) or
            (data[t] == target[0] and data[t+2] == target[2]) or 
            (data[t+2] == target[2] and data[t+1] == target[1])):
            return True
    return False

def isMoof1(moos,corruption):
    lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arr = []
    for t in moos:
        for letter in lowerCaseLetters:
            if letter != t[1]:
                t[0] = letter
                arr.append(deepCopy(t))
    for t in corruption:
        if t[0] == t[1]:
            for letter in lowerCaseLetters:
                if letter != t[1]:
                    t[0] = letter
                    arr.append(deepCopy(t))
            continue
        if t[0] == t[1]:
            t[1] == t[2]
            arr.append(deepCopy(t))
            continue 
        if t[0] == t[2]:
            t[2] == t[1]
            arr.append(deepCopy(t))
            continue
        var1 = t[1]
        t[1] = t[2]
        arr.append(deepCopy(t))
        t[2] = var1
        t[1] = var1
        arr.append(deepCopy(t))
    return arr

lengthOfStrings, frequency = map(int,input().split())
data = list(str(input()))
listOfMoos, f1 = uncorruptedMoos(data,lengthOfStrings)
if frequency != 1:
    moos, potentialMoos = isMoo(listOfMoos)
    for t in potentialMoos:
        if corruptedMoos(t,data):
            moos.append(t)
else:
    moos = isMoof1(listOfMoos, f1)
moos.sort()
print(len(moos))
for t in moos:
    printMoos(t)