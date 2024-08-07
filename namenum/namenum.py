"""
ID:alexand233
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
f = open('dict.txt', 'r')
fout = open ('namenum.out', 'w')
input1 = int(fin.readline().strip())
names_converted_into_numbers = []
acceptable_names = []
list_of_valid_names = []
letter_to_number = {'A':'2','B':'2','C':'2',
                    'D':'3','E':'3','F':'3',
                    'G':'4','H':'4','I':'4',
                    'J':'5','K':'5','L':'5',
                    'M':'6','N':'6','O':'6',
                    'P':'7','R':'7','S':'7',
                    'T':'8','U':'8','V':'8',
                    'W':'9','X':'9','Y':'9',
                    'Q':'0','Z':'0'}
while True:
    name = f.readline().strip()
    if not name:
        break
    list_of_valid_names.append(name)
    temporary_string = ""
    for x in range(len(name)):
        temporary_variable = letter_to_number.get(name[x])
        temporary_string = temporary_string + str(temporary_variable)
    names_converted_into_numbers.append(temporary_string)
for v in range(len(names_converted_into_numbers)):
    if input1 == int(names_converted_into_numbers[v]):
        acceptable_names.append(list_of_valid_names[v])
if len(acceptable_names) == 0:
    fout.write("NONE" + '\n')
for b in range(len(acceptable_names)):
    fout.write(acceptable_names[b] + '\n')
fout.close()
