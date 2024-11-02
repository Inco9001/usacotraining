"""
ID:alexand233
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
def create_graph(arr):
    print("hit")
    temp_arr = [arr[0]]
    if len(arr) <= 2:
        temp_arr.append(arr[1]) 
        return temp_arr
    arr.remove[arr[0]]
    for t in arr:
        temp_arr.append(t)
        arr.remove(t)
        return temp_arr.append(create_graph(arr)) 

num_wormholes = int(input())
array_of_wormholes = []
for t in range(num_wormholes):
    temp_arr = list(map(int,fin.readline().strip().split()))
    array_of_wormholes.append(temp_arr)
print(create_graph(array_of_wormholes))