fin = open('socdist1.in','r')
fout = open('socdist1.out','w')
length_of_string = int(fin.readline().strip())
string_of_cow_barns = fin.readline().strip()

def string_to_array(str):
    ret = []
    for i in str:
        ret.append(int(i))
    return ret

def deepcopy(arr):
    ret = []
    for i in arr:
        ret.append(i)
    return ret

def count_zeros(arr):
    ret = []
    current_count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            ret.append(current_count)
            current_count = 0
            continue
        current_count += 1
    ret.append(current_count)
    return ret

def add_cow(arr):
    max_index = 0
    max_value = 0
    for i in range(len(arr)):
        if (i == 0 or i == len(arr) -1) and arr[i] > max_value:
            max_index = i
            max_value = arr[i]
        elif arr[i]//2 > max_value:
            max_index = i
            max_value = arr[i] // 2
    
    ret = deepcopy(arr)
    if max_index == 0:
        ret.insert(0,0)
    elif max_index == len(arr) - 1:
        ret.append(0)
    else:
        old_value = ret[max_index]
        ret[max_index] = max_value
        ret.insert(max_index, old_value - max_value)
    return ret


# data setup
zero_count = count_zeros(string_to_array(string_of_cow_barns))
updated_count = []
for i in range(len(zero_count)):
    if i == 0 or i == len(zero_count)-1:
        updated_count.append(zero_count[i])
    else:
        updated_count.append(zero_count[i]+1)

# Data transformation
updated_count = add_cow(updated_count)
print(updated_count)
updated_count = add_cow(updated_count)
print(updated_count)

# Collecting correct final value
min_value = 1000000000000
for i in range(len(updated_count)):
    if i != 0 and i != len(updated_count) - 1 and updated_count[i] < min_value:
        min_value = updated_count[i]

if len(updated_count) == 3:
    min_value = updated_count[1] - 1

fout.write(str(min_value))
fout.close()
