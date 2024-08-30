"""
ID:alexand233
LANG: PYTHON3
TASK: milk2
"""
def deep_copy(input1):
    temp_array = []
    for t in range(len(input1)):
        temp_array.append(input1[t])
    return temp_array
def print_matrix(matrix):
    for i in range(len(matrix)):
        result_string = ""
        for j in range(len(matrix[i])):
            result_string += str(matrix[i][j]) + " "
        print(result_string)
            
def trimming(time_table):
    final_time_table = []
    final_time_table.append(deep_copy(time_table[0]))
    for t in range(1,len(time_table)):
        temp_array = []
        if final_time_table[-1][0] <= time_table[t][0] and time_table[t][0] <= final_time_table[-1][1]:
            temp_array.append(final_time_table[-1][0])
            temp_array.append(max(final_time_table[-1][1], time_table[t][1]))
            final_time_table.pop()
            final_time_table.append(deep_copy(temp_array))
        else:
            final_time_table.append(deep_copy(time_table[t]))
    return final_time_table

fin = open('milk2.in','r')
fout = open('milk2.out','w')
number_of_farmers = int(fin.readline().strip())
master_time_table = []
for t in range(number_of_farmers):
    farmer_time_table = list(map(int,fin.readline().strip().split()))
    master_time_table.append(farmer_time_table)
master_time_table.sort()
final_time_table = trimming(master_time_table)
#print(final_time_table)
max_time_milking = final_time_table[0][1] - final_time_table[0][0]
max_time_not_milking = 0
for t in range(len(final_time_table) - 1):
    temp_max_time_milking = final_time_table[t + 1][1] - final_time_table[t + 1][0]
    temp_max_time_not_milking = final_time_table[t + 1][0] - final_time_table[t][1]
    #print(str(final_time_table[t + 1][0]) + " " + str(final_time_table[t][1]))
    if temp_max_time_milking > max_time_milking:
        max_time_milking = temp_max_time_milking
    if temp_max_time_not_milking > max_time_not_milking:
        max_time_not_milking = temp_max_time_not_milking
fout.write(str(max_time_milking) + " " + str(max_time_not_milking) + '\n' )
fout.close()
        

