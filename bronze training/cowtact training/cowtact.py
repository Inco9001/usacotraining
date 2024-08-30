def total(array):
    final_answer = 0
    for t in array:
        final_answer += t
    return final_answer


def combine_ones(array):
    arr = []
    var = 0
    index = 0
    while True:
        if index < len(array) - 1 and array[index] == 0:
            index += 1
        else:
            break
    for t in range(index,len(array)):
        if array[t] == 1:
            var += 1
        elif array[t - 1] != 0:
            arr.append(var) 
            var = 0
    if var != 0:
        arr.append(var)
    return arr

def maxium_days(array,start,end):
    var = len(array)
    maxium_days_passed = []
    for t in range(var):
        if (t == 0 and start) or (t == var - 1 and end):
            maxium_days_passed.append(array[t] - 1)
            continue
        maxium_days_passed.append((array[t] - 1)//2)
    return min(maxium_days_passed)

def final_answer(array,max_days):
    final_answer = 0
    for t in array:
        if t%(2*max_days+1) == 0:
            final_answer += (t // (2*max_days+1))
        else:
            final_answer += (t // (2*max_days+1)) + 1
    return final_answer

num_cows = int(input().strip())
cow_states = str(input().strip().split())
list_of_cow_states = []
start = False
end = False

for t in range(2,num_cows + 2):
    list_of_cow_states.append(int(cow_states[t]))
if list_of_cow_states[0] == 1:
    start = True
if list_of_cow_states[-1] == 1:
    end = True
arr = combine_ones(list_of_cow_states)
if len(arr) == 0:
    print(0)
elif max(arr) == num_cows:
    print(1)
elif min(arr) < 2:
    print(total(arr))
else:
    days_passed = maxium_days(arr,start,end)
    print(final_answer(arr,days_passed))

"""
n day has passed
all cows are infected

1 - 3
2 - 5
3 - 7
4 - 9
n -> 2*n + 1

3 cows, 3 day has passed. Min inf cows -> 1
4 cows, 3 day -> 1
5 cows, 3 day -> 1
6 cows, 3 day -> 1
7 cows, 3 day -> 1
8 cows -> 2
9 cows -> 2
10 cows -> 2
Need 3 cows -> 15
Need 100 cows -> 694

You have a clump of x cows, and n days have passed. What is the minimum number of starting infected cows.

3 - 1
4 - 2
5 - 2
6 - 3
7 - 3
n -> n//2

3 - 2
4 - 3
5 - 4

n - 1

- Organize 0's/1's into array of clumps. Completed
- Find the maximum number of days that could have passed. Completed
    - max number of days is the smallest of the maximum number of days that could be applied to each clump.
    - 01110010 -> 2 clumps with max days 1 and max days 0. maximum number of days is 0.
    - 11100111011011 -> 4 clumps of maximum days of 2, 1, 0, 1. maximum number of days is 0
- find min cows for each clump for maximum number of days. Add together.
"""
