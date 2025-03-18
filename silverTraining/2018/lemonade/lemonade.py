fin = open("lemonade.in",'r')
fout = open("lemonade.out",'w')
numCows = int(fin.readline())
cowArr = list(map(int,fin.readline().split()))
cowArr.sort(reverse = True)
flag = True
print(cowArr)
for t in range(numCows):
    if cowArr[t] < t:
        fout.write(str(t)+"\n")
        flag = False
        break
if flag:
    fout.write(str(numCows)+"\n")