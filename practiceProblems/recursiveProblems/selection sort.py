def select_sort(arr):
    low = 0
    if 1 == len(arr):
        return arr[0]
    else:
        for x in range(len(arr)-2):
            if arr[x] < arr[low]:
                low = x
        var = arr[low]
        arr.remove(var)
        return str(var) + " " + str(select_sort(arr))
arr = list(map(int,input().split()))
print(select_sort(arr))