fin = open("num.in","r")
num_val = fin.readline().strip()
array = list(map(str,fin.readline().strip().split()))
for t in range(541):
    var = fin.readline().strip()
    for t in var:
        if t in array:
            continue
        print(var)
        break