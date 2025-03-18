def highestPower(num):
    t = 0
    while (10**t) <= num:
        t += 1  
    return t

def createLimit(power): 
    ans = 0
    for t in range(power):
        ans += 4*(10**(t))
    return ans

def quickSolveAid(power):
    ans = 0
    for t in range(2,power+1):
        ans += 5*(10**(t-2))
    return ans

def quickSolve(power):
    ans = 0 
    for t in range(1,power):
        if t == 1:
            continue
        ans += quickSolveAid(t)
    return ans 

def normRound(num):
    digits = list(str(num))
    numDigits = len(digits)
    if num%(10**(len(digits))) == 0:
        print(num)
        numDigits -= 1
    answer = num//(10**numDigits)
    if int(digits[-numDigits]) > 4:
        answer += 1
    answer = answer*(10**numDigits)
    return answer

def chainRound(num):
    answer = num
    digits = list(str(answer))
    numDigits = len(digits)
    if num%(10**(len(digits))) == 0:
        numDigits -= 1
    for t in range(1,numDigits+1):
        digits = list(str(answer))
        answer = answer//(10**t)
        if int(digits[-t]) > 4:
            answer += 1
        answer = answer*(10**t)
    return answer

def findDiscrepancies(lim,num):
    answer = 0
    for t in range(lim,num+1):
        #print(str(normRound(t,digits,numDigits))+ " " + str(chainRound(t,digits,numDigits)) + " " + str(t))
        if normRound(t) != chainRound(t):
            #print(str(normRound(t))+ " " + str(chainRound(t)) + " " + str(t))
            answer += 1
    return answer

numNum = int(input())
for t in range(numNum):
    currentNum = int(input())
    if currentNum < 45:
        print(str(0))
        continue
    power = highestPower(currentNum)
    limit = createLimit(power)
    if (10**power)//2 > currentNum and currentNum > limit:
        print(str(quickSolve(power) + findDiscrepancies(limit, currentNum)))
        continue
    print(str(quickSolve(power)))