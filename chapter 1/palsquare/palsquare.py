"""
ID:alexand233
LANG: PYTHON3
TASK: palsquare
"""
def final_print(number_array,original_number):
    conversion_array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I']
    temp_string2 = ""
    for t in range(len(original_number)):
        temp_string2 += conversion_array[original_number[t]]
    temp_string = temp_string2 + " "
    for t in range(len(number_array)):
        temp_string += conversion_array[number_array[t]]
    fout.write(temp_string + '\n')
    return  temp_string
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

fin = open('palsquare.in','r')
fout = open('palsquare.out','w')
base = int(fin.readline().strip())
for t in range(1,301):
    original_number = t
    base_10_number = t**2
    coverted_base = convert_base(base_10_number,base)
    converted_original_number = convert_base(original_number,base)
    if palindrome(coverted_base) != False:
        final_print(coverted_base,converted_original_number)
fout.close()