def turn_string_into_character_array(string):
    temp_array = []
    for t in range(len(string)):
        temp_array.append(string[t])
    return temp_array
def array_buffer(charracter_array_of_cow_barns):
    buffer = 0
    if character_array_of_cow_barns[0] != '1':
        while True:
            buffer += 1
            if character_array_of_cow_barns[buffer] != '0' or buffer + 1 == len(character_array_of_cow_barns):
                break
    return  buffer
def string_of_zeros(array,buffer):
    array_of_number_of_empty_stalls = []
    length_of_string = len(array)
    temp_int = 0
    for t in range(buffer + 1,length_of_string):
        temp_int += 1
        if character_array_of_cow_barns[t] == '1':
            array_of_number_of_empty_stalls.append(temp_int - 1)
            temp_int = 0
    array_of_number_of_empty_stalls.append(temp_int)
    return array_of_number_of_empty_stalls
fin = open('socdist1.in','r')
fout = open('socdist1.out','w')
length_of_string = int(fin.readline().strip())
string_of_cow_barns = fin.readline().strip()
character_array_of_cow_barns = turn_string_into_character_array(string_of_cow_barns)
array_of_number_of_empty_stalls = []
buffer = array_buffer(character_array_of_cow_barns)
flag = True
flag2 = True
array_of_number_of_empty_stalls = string_of_zeros(character_array_of_cow_barns,buffer)
temp_int = int(array_of_number_of_empty_stalls[-1])
if buffer > 0:
    array_of_number_of_empty_stalls.append(buffer)
    flag = False
if temp_int > 0:
    flag2 = False
else:
    array_of_number_of_empty_stalls.pop(-1)
for t in range(2):
    array_of_number_of_empty_stalls.sort()
    temp_int2 = int(array_of_number_of_empty_stalls[-1])
    array_of_number_of_empty_stalls.pop(-1)
    if temp_int2 == temp_int and flag2 == False:
        array_of_number_of_empty_stalls.append(temp_int2 - 1)
        flag2 = True
    elif temp_int2 == buffer and flag == False:
        array_of_number_of_empty_stalls.append(temp_int2 - 1)
        flag = True
    else:
        if temp_int2%2 != 1:
            array_of_number_of_empty_stalls.append(temp_int2//2 - 1)
            array_of_number_of_empty_stalls.append(temp_int2//2)
        else:
            array_of_number_of_empty_stalls.append(temp_int2//2)
            array_of_number_of_empty_stalls.append(temp_int2//2)
if flag2 == False:
    array_of_number_of_empty_stalls.remove(temp_int)
if flag == False:
    array_of_number_of_empty_stalls.remove(buffer)
fout.write(str(min(array_of_number_of_empty_stalls) + 1))
fout.close()