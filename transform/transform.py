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

def transformation1(matrix): # does a 90 degree rotation
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[t][input2 - x] = temp_array[x][t]
    return temp_array2
def transformation2(matrix): # does a 180 degree rotation 
    temp_array = transformation1(matrix)
    return transformation1(temp_array)
def transformation3(matrix): # does a 270 degree rotation 
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[input2 - t][x] = temp_array[x][t]
    return temp_array2

def transformation4(matrix): # does a horizontal flip 
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[x][input2 - t] = temp_array[x][t]
    return temp_array2
def transformation5(matrix): # does a horizontal flip and a 90 degree rotation
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[x][input2 - t] = temp_array[x][t]
    return transformation1(temp_array2)
def transformation6(matrix): # does a horizontal flip and a 180 degree rotation 
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[input2 - x][t] = temp_array[x][t]
    return transformation2(temp_array2)
def transformation7(matrix): # does a horizontal flip and a 270 degree rotation 
    input1 = len(matrix)
    temp_array = deepcopy(matrix)
    temp_array2 = empty_matrix(input1)
    input2 = input1 - 1 
    for x in range(input1):
        for t in range(input1):
            temp_array2[x][input2 - t] = temp_array[x][t]
    return transformation3(temp_array2)

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

if deep_equals(transformation1(starting_array),end_array):
    fout.write('1' + '\n')
elif deep_equals(transformation2(starting_array),end_array):
    fout.write('2' + '\n')
elif deep_equals(transformation3(starting_array),end_array):
    fout.write('3' + '\n')
elif deep_equals(transformation4(starting_array),end_array):
    fout.write('4' + '\n')
elif deep_equals(transformation5(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(transformation6(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(transformation7(starting_array),end_array):
    fout.write('5' + '\n')
elif deep_equals(end_array,starting_array):
    fout.write('6' + '\n')
else:
    fout.write('7' + '\n')

print(transformation4(starting_array))