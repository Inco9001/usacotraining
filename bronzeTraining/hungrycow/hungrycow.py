# fin = open("hungrycow.in", 'r')

firstline = input().split()

numberOfInput = int(firstline[0])
numberOfDays = int(firstline[1])

# print(numberOfInput)
# print(numberOfDays)

leftoverBales = 0
currentDay = 1
daysEaten = 0
for i in range(numberOfInput):
    nextline = input().split()
    daymarker = int(nextline[0])
    deliveredbales = int(nextline[1])
    dayspassed = daymarker - currentDay
    eaten = min(leftoverBales, dayspassed)
    leftoverBales = leftoverBales - eaten + deliveredbales
    currentDay = daymarker
    daysEaten = daysEaten + eaten

endOfSeasonEating = numberOfDays - currentDay + 1
daysEaten = daysEaten + min(leftoverBales, endOfSeasonEating)
print(daysEaten)