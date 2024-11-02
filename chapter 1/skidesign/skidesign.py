"""
ID:alexand233
LANG: PYTHON3
TASK: skidesign
"""
def compute_average(arr,median):
    ans = 0
    median2 = median + 17
    if median + 17 > arr[-1]:
        median2 = arr[-1]
    for t in range(len(arr)):
        if arr[t] < median:
            ans += (median - arr[t])**2
        elif arr[t] > median2:
            ans += (arr[t] - median2)**2
    return ans
def compute_all_possible_averages(arr):
    array = []
    for t in range(1001):
        array.append(compute_average(arr,t))
    return min(array)
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')
number_of_hills = int(fin.readline().strip())
array_of_mountains = []
for t in range(number_of_hills):
    array_of_mountains.append(int(fin.readline().strip()))
array_of_mountains.sort()
fout.write(str(compute_all_possible_averages(array_of_mountains)) + "\n")
fout.close() 
