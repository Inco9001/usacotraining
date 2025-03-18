def feedNeeded():
    ans = 0
    # numCows = int(fin.readline())
    # cows = list(map(int,fin.readline().split()))
    numCows = int(input())
    cows = list(map(int,input().split()))
    while max(cows) != min(cows):
        if cows[0] > cows[1] or cows[-1] > cows[-2]:
            return -1
        for t in range(numCows-2):
            difference1 = cows[t+1] - cows[t]
            difference2 = cows[t+1] - cows[t+2]
            if difference1 > cows[t+2] or difference2 > cows[t] or min(cows) < 0:
                return -1
            if difference1 > 0:
                cows[t+1] -= difference1
                cows[t+2] -= difference1
                ans += difference1
            if difference2 > 0:
                cows[t+1] -= difference2
                cows[t] -= difference2
                ans += difference2

    return ans*2
# fin = open('feed.in','r')
testCases = int(input())
for t in range(testCases):
    print(feedNeeded())
