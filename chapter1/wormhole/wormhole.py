"""
ID:alexand233
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
def deepCopy(arr):
    temp_arr = []
    for t in range(len(arr)):
        temp_arr.append(arr[t])
    return temp_arr

def create_graph(arr):
    temp_arr = [arr[0]]
    final_arr = []
    arr.pop(0)
    if len(arr) > 2:
        for t in arr:
            recursive_arr = deepCopy(arr)
            temp_arr.append(t)
            recursive_arr.remove(t)
            final_arr.append(deepCopy(temp_arr))
            final_arr.append(create_graph(recursive_arr))
            temp_arr.remove(t)
        return final_arr
    temp_arr.append(arr[-1]) 
    return temp_arr
    

num_wormholes = int(fin.readline().strip())
array_of_wormholes = []
for t in range(num_wormholes):
    temp_arr = list(map(int,fin.readline().strip().split()))
    array_of_wormholes.append(temp_arr)
print(create_graph(array_of_wormholes))
print(array_of_wormholes)