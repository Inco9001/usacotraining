"""
ID:alexand233
LANG: PYTHON3
TASK: pprime
"""
fin = open("pprime.in",'r')
fout = open('pprime.out','w')

import math

def isPrime(num):
    flag = True
    t = 2
    while t <= math.sqrt(num):
        if num%t == 0:
            flag = False
            break
        t += 1
    return flag
def generatePalindromes():
    primePalindromes = [2,3,5,7,11]
    palindromeArr = []
    for t in range(10):
        if (t%2 == 0 or t%5 == 0) and t != 0:
            continue
        for x in range(10):
            for y in range(10):
                for z in range(10):
                    palindrome = ""
                    if t == 0:
                        if (x%2 == 0 or x%5 == 0) and x != 0:
                            continue
                        if x == 0:
                            if (y%2 == 0 or y%5 == 0):
                                continue
                            else:
                                palindrome = int(str(y) + str(z) +str(y))
                        else:                   
                            palindrome = int(str(x) + str(y) + str(z) + str(y) + str(x))
                    else:
                        palindrome = int(str(t) + str(x) + str(y) + str(z) +str(y) + str(x) + str(t))
                    palindromeArr.append(palindrome)
    for t in palindromeArr:
        if isPrime(t):
            primePalindromes.append(t)
    return primePalindromes

primePalindromes = generatePalindromes()
floor,ceiling = map(int,fin.readline().split())
for t in primePalindromes:
    if t < floor:
        continue
    if t > ceiling:
        break
    fout.write(str(t) + "\n")
            