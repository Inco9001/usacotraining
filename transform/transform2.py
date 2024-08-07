"""
ID:alexand233
LANG: PYTHON3
TASK: transform
"""
def deep_equals(matrix1,matrix2):
    ret = True
    input1 = len(matrix1)
    for t in range(input1):
        for x in range(input1):
            ret = ret and matrix1[t][x] == matrix2[t][x]
    return ret
                
def print_pretty(matrix):
    input1 = len(matrix)
    for t in range(input1):
        print(matrix[t])
def deepcopy(matrix):
    temp_array = []
    len_matrix = len(matrix)
    for t in range(len_matrix):
        temp_array2 = []
        for x in range(len_matrix):
            temp_array2.append(matrix[t][x])
        temp_array.append(temp_array2)
    return temp_array
def empty_matrix(input1):
    temp_array = []
    for t in range(input1):
        temp_array2 = []
        for x in range(input1):
            temp_array2.append(0)
        temp_array.append(temp_array2)
    return temp_array

def ninety_degree_rotation(matrix): # does a 90 degree rotation
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[t][input2 - x] = temp_array[x][t]
    return temp_array2

def horizontal_flip(matrix): # does a horizontal flip 
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[x][input2 - t] = temp_array[x][t]
    return temp_array2
def trans1(matrix):
    return ninety_degree_rotation(matrix)
def trans2(matrix):
    temp_array = ninety_degree_rotation(matrix)
    return ninety_degree_rotation(temp_array)
def trans3(matrix):
    temp_array = ninety_degree_rotation(matrix)
    temp_array = ninety_degree_rotation(temp_array)
    return ninety_degree_rotation(temp_array)
def trans4(matrix):
    return horizontal_flip(matrix)
def trans5(matrix):
    temp_array = horizontal_flip(matrix)
    return trans1(temp_array)
def trans6(matrix):
    temp_array = horizontal_flip(matrix)
    return trans2(temp_array)
def trans7(matrix):
    temp_array = horizontal_flip(matrix)
    return trans3(temp_array)
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
input1 = int(fin.readline().strip())
starting_array = []
end_array = []
for t in range(input1):
    tempstring = list(fin.readline().strip())
    starting_array.append(tempstring)
for t in range(input1):
    tempstring = list(fin.readline().strip())
    end_array.append(tempstring)
if deep_equals(trans1(starting_array),end_array):
    fout.write('1' + '\n')
elif deep_equals(trans2(starting_array),end_array):
    fout.write('2' + '\n')
elif deep_equals(trans3(starting_array),end_array):
    fout.write('3' + '\n')
elif deep_equals(trans4(starting_array),end_array):
    fout.write('4' + '\n')
elif deep_equals(trans5(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(trans6(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(trans7(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(end_array,starting_array):
    fout.write('6' + '\n')
else:
    fout.write('7' + '\n')





