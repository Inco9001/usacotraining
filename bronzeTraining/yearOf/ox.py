fin = open("ox.in","r")

years = {"Ox":0, "Tiger":1, "Rabbit":2, "Dragon":3, "Snake":4, "Horse":5, "Goat":6, "Monkey":7, "Rooster":8, "Dog":9, "Pig":10, "Rat":11}

numConnections = int(fin.readline())

var = list(map(str,fin.readline().strip().split()))
print(var)