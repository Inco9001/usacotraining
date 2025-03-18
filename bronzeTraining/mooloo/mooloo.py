firstline = input().split()
k = int(firstline[1])
days = input().split()

cost = k+1
currentday = int(days[0])

for i in range(1, len(days)):
    value = int(days[i])
    extend = value-currentday
    new = k+1
    cost = cost + min(extend, new)
    currentday = value

print(cost)