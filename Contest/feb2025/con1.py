fin = open("con.in","r")
canvasSize, changes = map(int,fin.readline().split())
differnces = [0,0,0,0]
canvas = []
for t in range(canvasSize):
    canvas.append(list(map(str,fin.readline().strip())))
def matches(var):
    for y in range(var):
        for x in range(var):
            if canvas[y][x] != canvas[y][-1-x]:
                differnces[0] += 1
                differnces[1] += 1
    for y in range(var):
        for x in range(var):
            if canvas[y][x] != canvas[-1-y][x]:
                differnces[0] += 1
                differnces[2] += 1
    for y in range(var):
        for x in range(var):
            if canvas[y][x] != canvas[-1-y][-1-x]:
                differnces[0] += 1
                differnces[3] += 1
    for y in range(var):
        for x in range(var):
            if canvas[y][-1-x] != canvas[-1-y][x]:
                differnces[1] += 1
                differnces[2] += 1
    for y in range(var):
        for x in range(var):
            if canvas[y][-1-x] != canvas[-1-y][-1-x] :
                differnces[1] += 1
                differnces[3] += 1
    for y in range(var):
        for x in range(var):
            if canvas[-1-y][x] != canvas[-1-y][-1-x]:
                differnces[2] += 1
                differnces[3] += 1
    return 

def change(quad,x,y):
    flag = 0
    if quad == 1:
        if canvas[y][x] == canvas[y][-1-x]:
            differnces[1] -= 1
            differnces[0] -= 1
        else:
            differnces[1] += 1
            differnces[0] += 1
        if canvas[y][x] == canvas[-1-y][x]:
            differnces[0] -= 1
            differnces[2] -= 1
        else:
            differnces[2] += 1
            differnces[0] += 1
        if canvas[y][x] == canvas[-1-y][-1-x]:
            differnces[0] -= 1
            differnces[3] -= 1
        else:
            differnces[3] += 1
            differnces[0] += 1
            
    elif quad == 2:
        if canvas[y][x] == canvas[y][-1-x]:
            differnces[0] -= 1
            differnces[1] -= 1
        else:
            differnces[0] += 1
            differnces[1] += 1
        if canvas[y][x] == canvas[-1-y][-1-x]:
            differnces[2] -= 1
            differnces[1] -= 1
        else:
            differnces[2] += 1
            differnces[1] += 1
        if canvas[y][x] == canvas[-1-y][x]:
            differnces[3] -= 1
            differnces[1] -= 1
        else:
            differnces[3] += 1
            differnces[1] += 1

    elif quad == 3:
        if canvas[y][x] == canvas[-1-y][x]:
            differnces[0] -= 1
            differnces[2] -= 1
        else:
            differnces[0] += 1
            differnces[2] += 1
        if canvas[y][x] == canvas[-1-y][-1-x]:
            differnces[1] -= 1
            differnces[2] -= 1
        else:
            differnces[1] += 1
            differnces[2] += 1
        if canvas[y][x] == canvas[y][-1-x]:
            differnces[3] -= 1
            differnces[2] -= 1
        else:
            differnces[3] += 1
            differnces[2] += 1

    else:
#        print(differnces)

        if canvas[y][x] == canvas[-1-y][-1-x]:
            differnces[0] -= 1
            differnces[3] -= 1
        else:
            differnces[0] += 1
            differnces[3] += 1
        if canvas[y][x] == canvas[-1-y][x]:
            differnces[1] -= 1
            differnces[3] -= 1
        else:
            differnces[1] += 1
        if canvas[y][x] == canvas[y][-1-x]:
            differnces[2] -= 1
            differnces[3] -= 1
        else:
            differnces[2] += 1
            differnces[3] += 1
    print(min(differnces))
    return
var = canvasSize//2 
matches(var)
print(min(differnces))
for t in range(changes):
    quadrant = 0
    y,x = map(int,fin.readline().split())
    x -= 1
    y -= 1
    if canvas[y][x] == "#":
        canvas[y][x] = "."
    else:
        canvas[y][x] = "#"
    
    if x < var and y < var:
        quadrant = 1
    elif x >= var and y < var:
        quadrant = 2
    elif x < var and y >= var:
        quadrant = 3
    else:
        quadrant = 4
    change(quadrant,x,y)



