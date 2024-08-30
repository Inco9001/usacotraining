"""
ID:alexand233
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')
def calculate_changes(arr):
    change = []
    temp_arr = []
    while arr[-1] - arr[0] > 17 and arr[-2] - arr[1] > 17:
        total_change = arr[-1] - arr[0] - 17
        if total_change < 1: 
            arr.pop(-1)
            continue
        change.append(total_change//2)
        temp_arr.append(arr[-1] - total_change//2)
        arr[0]
        if total_change%2 == 0:
            change.append(total_change//2)
            temp_arr.append(arr[0] + total_change//2)
            arr.pop(-1)
        else:
            change.append(total_change//2 + 1)
            temp_arr.append(arr[0] + total_change//2 + 1)
        arr.pop(0)
    temp_arr.sort()
    print(temp_arr)
        
    return change

def calculate_final_price(arr1):
    final_answer = 0
    arr = calculate_changes(arr1)
    for t in range(len(arr)):
        final_answer += arr[t]**2
    return final_answer

number_of_hills = int(fin.readline().strip())
array_of_mountains = []
for t in range(number_of_hills):
    array_of_mountains.append(int(fin.readline().strip()))
array_of_mountains.sort()
if array_of_mountains[-1] - array_of_mountains[0] < 18:
    fout.write(str(0) + '\n')
else:
    fout.write(str(calculate_final_price(array_of_mountains)) + '\n')
fout.close() 
