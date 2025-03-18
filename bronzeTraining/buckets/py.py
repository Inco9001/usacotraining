location = {"bx":0,"by":0,"lx":0,"ly":0,"rx":0,"ry":0}

fin = open("py.in","r")
canvas = []
for t in range(10):
    canvas.append([])
    temp = map(str,fin.readline().strip())
    for i in temp:
        canvas[t].append(i)
for t in range(10):
    for i in range(10):
        if canvas[t][i] == "B":
            location["bx"] = i
            location["by"] = t
        if canvas[t][i] == "L":
            location["lx"] = i
            location["ly"] = t
        if canvas[t][i] == "R":
            location["rx"] = i
            location["ry"] = t
print(location)