"""
ID:alexand233
LANG: PYTHON3
TASK: dualpal
"""
def palindrome(number_array):
    flag = True
    length_of_array = len(number_array)
    for t in range(length_of_array//2):
        if number_array[t] != number_array[length_of_array - t - 1]:
            flag = False
            break
    return flag

def convert_base(number,base):
    temp_num = number//base
    temp_num2 = number%base
    temp_array = []
    temp_array.append(temp_num2)
    while True:
        if temp_num == 0:
            break
        temp_num2 = temp_num%base
        temp_array.insert(0,temp_num2)
        temp_num = temp_num//base
    return temp_array
fin = open('dualpal.in','r')
fout = open('dualpal.out','w')
num_of_palindromes_required,starting_number = map(int,fin.readline().strip().split())
starting_number += 1
final_answers = []
num_of_palindromes_found = 0
while num_of_palindromes_found < num_of_palindromes_required:
    temp_num_of_palindromes_found = 0
    for t in range(2,11):
        if temp_num_of_palindromes_found >= 2:
            break
        if palindrome(convert_base(starting_number,t)) == True:
            temp_num_of_palindromes_found += 1
    if temp_num_of_palindromes_found >= 2:
        num_of_palindromes_found += 1
        final_answers.append(str(starting_number)) 
    starting_number += 1
for t in range(num_of_palindromes_required):
    fout.write(final_answers[t] + '\n')
fout.close()