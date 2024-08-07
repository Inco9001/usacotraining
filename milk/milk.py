"""
ID:alexand233
LANG: PYTHON3
TASK: milk
"""
def trim(matrix,total_cost,number_of_farmers,total_milk,total_milk_collected):
    temp_value = total_cost - (matrix[number_of_farmers - 1][1]*matrix[number_of_farmers - 1][0])
    required_units = total_milk - (total_milk_collected - matrix[number_of_farmers - 1][1])
    temp_value += required_units*matrix[number_of_farmers - 1][0]
    return temp_value
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
total_milk,max_farmers = map(int,fin.readline().strip().split())
number_of_farmers = 0
total_cost = 0
total_milk_collected = 0
matrix = []

while True:
    data = list(map(int,fin.readline().strip().split()))
    if len(data) == 0: 
        break
    else:
        matrix.append(data)
matrix.sort()
for t in range(len(matrix)):
    if number_of_farmers > max_farmers:
        break
    if total_milk_collected < total_milk:
        number_of_farmers += 1
        total_milk_collected += matrix[t][1]
        total_cost  += matrix[t][1] * matrix[t][0]
        continue
    break
print(matrix.index([3,10]))
if total_milk_collected < total_milk:
    
    print()
print(trim(matrix,total_cost,number_of_farmers,total_milk,total_milk_collected))