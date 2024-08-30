
def maxium_radius(matrix):
    max_radius = matrix[-1][0]
    number_of_cows = len(matrix)
    for t in range(number_of_cows - 1):
        if matrix[t][1] != matrix[t + 1][1]:
            max_radius = min((matrix[t+1][0] - matrix[t][0]),max_radius)

    return max_radius

def boundary_case_1(matrix):
    flag = True
    for t in range(len(matrix)):
        if matrix[t][1] == 0:
            flag = False
            break 
    return flag

def boundary_case_2(matrix):
    flag = True
    for t in range(len(matrix)):
        if matrix[t][1] == 1:
            flag = False
            break
    return flag

def to_first_1(matrix):
    var = 0
    for t in range(len(matrix)):
        if matrix[t][1] == 1:
            break
        var += 1 
        
    return var

def to_last_1(matrix):
    var = len(matrix)
    temp_var = 0
    for t in range(1, var + 1):
        if matrix[var - t][1] == 1:
            break
        temp_var += 1
    temp_var = var - temp_var
    return temp_var

def clustering(matrix,max_radius):
    number_of_clusters = 1
    start = to_first_1(matrix)
    end = to_last_1(matrix)
    var = start
    for t in range(start,end):
        if matrix[t][1] == 1: 
            if matrix[t][0] - matrix[var][0] > max_radius - 1: 
                number_of_clusters += 1
            var = t
    return number_of_clusters

def answer(matrix):
    all_infected = boundary_case_1(matrix)
    all_not_infected = boundary_case_2(matrix)
    final_answer = 0
    if all_infected == False and all_not_infected == False:
        final_answer = clustering(matrix,maxium_radius(matrix))
    elif all_infected == True:
        final_answer = 1
        
    return final_answer

fin = open('socdist2.in','r')
fout = open('socdist2.out','w')
number_of_cows = int(fin.readline().strip())
cows_postions_and_state = []
for t in range(number_of_cows):
    arr = list(map(int,fin.readline().strip().split()))
    cows_postions_and_state.append(arr)
cows_postions_and_state.sort()
fout.write(str(answer(cows_postions_and_state)) + '\n')
fout.close()
