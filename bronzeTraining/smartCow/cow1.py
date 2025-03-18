# fin = open("cow.in",'r')
# numPapers, adjustments = map(int,fin.readline().strip().split())
# papers = list(map(int,fin.readline().strip().split()))
numPapers, adjustments = map(int,input().strip().split())
papers = list(map(int,input().strip().split()))
papers.sort(reverse = True)
hScore = 0
for t in range(numPapers):
    if papers[t] >= hScore + 1:
        hScore += 1
        continue
    if papers[t] >= hScore and adjustments > 0:
        hScore += 1
        continue
    break
if papers[hScore-1] == papers[hScore-2] and adjustments == 1:
    hScore -= 1
print(hScore)