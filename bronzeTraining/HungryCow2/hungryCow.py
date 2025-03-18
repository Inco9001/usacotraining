foodDeliveries, days = map(int,input().strip().split())
onsiteFood = 0
foodEaten = 0
lastDelivery = 0
for t in range(foodDeliveries):
    dayDelivered, foodAmount = map(int,input().strip().split())
    dayDifference = dayDelivered - lastDelivery
    if onsiteFood < dayDifference:
        foodEaten += onsiteFood + 1
        onsiteFood = foodAmount - 1
    else:
        foodEaten += dayDifference
        onsiteFood = onsiteFood - dayDifference + foodAmount
    lastDelivery = dayDelivered
if lastDelivery < days and onsiteFood > 0:
    if onsiteFood >= (days-lastDelivery):
        foodEaten += days - lastDelivery
    else:
        foodEaten += onsiteFood
print(foodEaten)