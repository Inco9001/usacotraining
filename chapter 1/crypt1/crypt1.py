"""
ID: your_id_here
LANG: PYTHON3
TASK: crypt1
"""
def toString(array):
    var = ""
    for t in array:
        var += str(t)
    return var
def is_vaild(array,arr):
    abc = array[0]
    d = array[1]
    e = array[2]
    var1 = int(abc)*(int(d)*10)
    var2 = int(abc)*int(e)
    var = str(var1 + var2)
    flag = True
    if len(var) == 4 and len(str(var1//10)) == 3 and len(str(var2)) == 3:
        for t in var:
            if int(t) in arr:
                continue
            flag = False
            break
        for t in str(var1//10): 
            if int(t) in arr:
                continue
            flag = False
            break
        for t in str(var2):
            if int(t) in arr:
                continue
            flag = False
            break
    else:
        flag = False
    return flag
def valid_combos(array):
    num = 0
    for a in array:
        for b in array:
            for c in array:
                for d in array:
                    for e in array: 
                        arr1 = []
                        arr1.append(toString([a,b,c]))
                        arr1.append(d)
                        arr1.append(e)
                        if is_vaild(arr1,array):
                            num += 1
                            
    return num              
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
num_of_num = int(fin.readline().strip())
list_of_num = list(map(int,fin.readline().strip().split()))
list_of_num.sort()
num_valid_combos = valid_combos(list_of_num)
fout.write(str(num_valid_combos) + "\n")
fout.close()