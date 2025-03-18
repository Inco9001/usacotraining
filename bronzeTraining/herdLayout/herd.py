
correctLayout = []
for t in range(3):
    list1 = list(str(input()).strip())
    for x in list1:
        correctLayout.append(x)
givenLayout = []
for t in range(3):
    list1 = list(str(input()).strip())
    for x in list1:
        givenLayout.append(x)
correct = 0
inThere = 0
for t in range(9):
    if correctLayout[t] == givenLayout[t]:
        correct += 1
for t in givenLayout:
    if t in correctLayout:
        correctLayout.remove(t)
        inThere += 1
print(correct)
print(inThere-correct)
