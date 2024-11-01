"""
ID: your_id_here
LANG: PYTHON3
TASK: crypt1
"""
def toString(array):
    var = ""
    for t in var:
        var += str(t)
    return var
def is_vaild(array):

    return
def valid_combos(array):
    arr = []
    buffer = 0
    for a in array:
        for b in array:
            for c in array:
                for d in array:
                    for e in array: 
                        arr1 = []
                        arr1.append(toString([a,b,c]))
                        arr1.append(toString([e,d]))


    return arr 
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
num_of_num = int(fin.readline().strip())
list_of_num = list(map(int,fin.readline().strip().split()))
list_of_num.sort()
fout.close()