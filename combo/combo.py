"""
ID:alexand233
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w') 

def deepcopy(arr):
    final_arr = []
    for t in range(len(arr)):
        final_arr.append(arr[t])
    return final_arr

def generate_all_values(val1,val2,input1):
    final_array = []
    temp_array = [val1 - 2, val1 - 1, val1, val1 + 1, val1 + 2]
    for t in range(5):
        if temp_array[t] < 1:
            temp_array[t] += input1
        elif temp_array[t] > input1:
            temp_array[t] -= input1
    final_array.append(deepcopy(temp_array))
    temp_array = [val2 - 2, val2 - 1, val2, val2 + 1, val2 + 2]
    for t in range(5):
        if temp_array[t] < 1:
            temp_array[t] += input1
        elif temp_array[t] > input1:
            temp_array[t] -= input1
    final_array.append(deepcopy(temp_array))
    final_answer = intersection(final_array)

    return final_answer
def intersection(matrix):
    common_values = 0
    arr1 = matrix[0]
    arr2 = matrix[1]
    for t in range(len(arr1)):
        for x in range(len(arr1)):
            if arr1[t] == arr2[x]:
                common_values += 1
                break

    return common_values


size_of_lock = int(fin.readline().strip())
john_lock = list(map(int,fin.readline().strip().split()))
master_lock = list(map(int,fin.readline().strip().split()))
final_answer = 250
if size_of_lock < 5:
    final_answer = size_of_lock**3
elif john_lock == master_lock:
    final_answer = 125
else:
    temp_arr = []
    for t in range(3):
        var = generate_all_values(john_lock[t],master_lock[t],size_of_lock)
        temp_arr.append(var)
    var = 1
    for t in range(3):
        var = var*temp_arr[t]    
    final_answer -= var

fout.write(str(final_answer) + '\n')
fout.close