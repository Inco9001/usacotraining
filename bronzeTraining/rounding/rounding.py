# finds p in 10^p so we know our target rounding number for n 
def findTarget(num):
    ans = 0 
    while 10**ans < num:
        ans += 1
    return ans

# creates the first number where chain rounding and normal rounding disagree
def createLowerBound(num):
    ans = ""
    for t in range(num-1):
        ans += "4"
    ans += "5"
    return int(ans)

# produces an answer assuming that the size of P -2 will equal 55555555....p-2 times
def createAnswer(num):
    if num < 1:
        return 0
    ans = "0"
    for t in range(num):
        ans += "5"
    return int(ans) + createAnswer(num-1)

# finds the number of numbers from 1 to N where when rounded normal differers from chain rounding
def findDiscrepancies(num):
    targetNum = findTarget(num)
    lowerBound = createLowerBound(targetNum)
    if num < lowerBound:
        return createAnswer(targetNum-2)
    if num < (10**targetNum)//2:
        ans = createAnswer(targetNum-2)
        ans += num - lowerBound + 1
        return ans
    return createAnswer(targetNum-1)


testCases = int(input())
for t in range(testCases):
    num = int(input())
    ans = findDiscrepancies(num)
    print(ans)