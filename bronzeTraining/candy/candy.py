"""
list of inputs
3 2
3 2 5
6 1
"""
num_cows, num_canes = map(int,input().strip().split())
cow_heights = list(map(int,input().strip().split()))
cane_heights = list(map(int,input().strip().split()))
for t in range(num_canes):
    eaten_cane = 0
    cow_index = 0
    current_max_height = cane_heights[t]
    while eaten_cane < current_max_height and cow_index < num_cows:
        var = cow_heights[cow_index]
        if eaten_cane < var:
            if var >= current_max_height:
                cow_heights[cow_index] += current_max_height - eaten_cane
                eaten_cane += current_max_height - eaten_cane
                break
            else:
                cow_heights[cow_index] += var - eaten_cane
                eaten_cane += var - eaten_cane
        cow_index += 1 
for t in cow_heights:
    print(str(t))

