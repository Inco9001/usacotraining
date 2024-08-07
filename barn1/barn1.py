"""
ID:alexand233
LANG: PYTHON3
TASK: barn1
"""
fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w') 
def maxes(array,num_maxes):
    arr = []
    arr2 = deep_copy(array)
    for t in range(num_maxes - 1):
        var = max(arr2)
        arr.append(arr2.index(var))
        arr2.insert(arr2.index(var),0)
        arr2.remove(var)
    arr.sort()
    return arr
def deep_copy(array):
    arr = []
    for t in range(len(array)):
        arr.append(array[t])
    return arr
def find_gaps(array):
    temp_array = []
    for t in range(len(array) - 1):
        var = array[t + 1] - array[t]
        temp_array.append(var)
    return temp_array
def find_min_length(array_of_gaps,array_of_occupid_stalls,max_boards):
    final_answer = 0
    previous_segment = 0 
    index = 0
    array_of_maxes = maxes(array_of_gaps,max_boards)
    for t in range(max_boards - 1):
        current_segment = array_of_maxes[index]
        var = array_of_occupid_stalls[current_segment] - array_of_occupid_stalls[previous_segment]
        final_answer += var + 1
        previous_segment = current_segment + 1
        index += 1
    final_answer += array_of_occupid_stalls[-1] - array_of_occupid_stalls[previous_segment] + 1
    return final_answer
max_boards,total_number_of_stalls,number_of_occupied_stalls = map(int,fin.readline().strip().split())
if max_boards < number_of_occupied_stalls:
    array_of_occupid_stalls = []
    for t in range(number_of_occupied_stalls):
        array_of_occupid_stalls.append(int(fin.readline().strip()))
    array_of_occupid_stalls.sort()
    gaps_between_cows = find_gaps(array_of_occupid_stalls)
    final_answer = find_min_length(gaps_between_cows,array_of_occupid_stalls,max_boards)
    fout.write(str(final_answer) + '\n')
else:
    fout.write(str(number_of_occupied_stalls) + '\n')    
fout.close()