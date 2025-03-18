import time

start_time = time.time()

fin = open("cowHealth.in","r")

def makeArr(int):
    arr = []
    for t in range(int):
        arr.append(0)
    return arr

#outputs a binary string of how many cows would be checked in this new order. Matching is the new array Matched is the original array
#matching's first 2 characters are used for locational information in the original array
def matches(matched,matching):
    newArr = [matching[0],matching[1]]
    for t in range(2,matching[1]+2):
        if matching[t] == matched[t+matching[0]-2]:
            newArr.append(1)
            continue
        newArr.append(0)
    return newArr

#compares old and new binary strings to see the change in cows checked. 
#It should be noted the second binary string's first 2 characters are used to find computation location
def order(preComputed,postcompute):
    ChangesInCowsChecked = 0
    for t in range(2,postcompute[1]+2):
        if postcompute[t] == 1 and preComputed[t-2+postcompute[0]] == 0:
            ChangesInCowsChecked += 1
        if postcompute[t] == 0 and preComputed[t-2+postcompute[0]] == 1:
            ChangesInCowsChecked -= 1
    return ChangesInCowsChecked

#outputs a binary string of cows that will be checked even if no cow is moved and the number of cows checked initially
def findMatchs(cowArr,cowOrder,lenArr):
    numMatchs = 0
    arrMatchs = []
    for t in range(lenArr):
        if cowArr[t] == cowOrder[t]:
            numMatchs += 1
            arrMatchs.append(1)
            continue
        arrMatchs.append(0)
    return numMatchs,arrMatchs

numberOfCows = int(fin.readline())
cowArr = list(map(int,fin.readline().split()))
cowOrder = list(map(int,fin.readline().split()))
# arrMatchs is a binary string showing if there were any matches in the initial two arrs represented by a 1
numMatchs, arrMatchs = findMatchs(cowArr,cowOrder,numberOfCows)
arrOfCowsChecked = makeArr(numberOfCows+1)
for t in range(numberOfCows):
    i = 1
    # newCowArr will store three types of values. 1st is where the flip occurs aka the left most affected element.
    # second how many characters that were affected. Third are all the values.
    newCowArr = [t,1,cowArr[t]]
    # adds cases of no flip
    arrOfCowsChecked[numMatchs] += 1
    
    # cyles from nucleus to the ends of the array
    while t-i > -1 and t+i < numberOfCows:
        l = t-i
        r = t+i
        # code to insert the reversed array into the newCowArr array
        newCowArr.insert(newCowArr[1]+2,cowArr[l])
        newCowArr.insert(2,cowArr[r]) 
        # ensures that I have the right start point in the array
        newCowArr[0] = l
        #note that with each additional computation the number of affected numbers goes up by 2
        newCowArr[1] += 2
        val = order(arrMatchs,matches(cowOrder,newCowArr))
        arrOfCowsChecked[val+numMatchs] += 1
        i += 1
    
for t in range(numberOfCows-1):
    i = 1
    # newCowArr will store three types of values. 1st is where the flip occurs aka the left most affected element.
    # second how many characters that were affected. Third are all the values.
    newCowArr = [t,2,cowArr[t+1],cowArr[t]]
    # adds cases of no flip
    arrOfCowsChecked[order(arrMatchs,matches(cowOrder,newCowArr))+numMatchs] += 1
    # cyles from nucleus to the ends of the array
    while t-i > -1 and t+i < numberOfCows-1:
        l = t-i
        r = t+i+1

        # code to insert the reversed array into the newCowArr array
        newCowArr.insert(newCowArr[1]+2,cowArr[l])
        newCowArr.insert(2,cowArr[r])

        #note that with each additional computation the number of affected numbers goes up by 2
        newCowArr[1] += 2
        # ensures that I have the right start point in the array
        newCowArr[0] = l
        val = order(arrMatchs,matches(cowOrder,newCowArr))
        arrOfCowsChecked[val+numMatchs] += 1
        i += 1

for t in arrOfCowsChecked:
    print(t)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")