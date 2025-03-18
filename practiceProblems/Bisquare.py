import time

# ans = []
# var = int(input())
# for t in range(var+1):
#     for x in range(t+1):
#         ans.append(x**2+t**2)
# ans.sort()
# final = 0
# for t in range(1,len(ans)):
#     if ans[t-1] == ans[t]:
#         final += 1
# print(final)
# print(len(ans)-final)


# Naive Solution
start_time = time.time()
bisquares = []
for i in range(0, 251):
    for j in range(0, 251):
        k = i * i + j * j
        if k not in bisquares:
            bisquares.append(k)
end_time = time.time()
print("Naive Solution")
print(f"Answer: {len(bisquares)} Time: {end_time-start_time} seconds.")

# Naive Solution
start_time = time.time()
bisquares = []
for i in range(0, 251):
    for j in range(0, i + 1):
        k = i * i + j * j
        if k not in bisquares:
            bisquares.append(k)
end_time = time.time()
print("Naive Solution with minimal optimization")
print(f"Answer: {len(bisquares)} Time: {end_time-start_time} seconds.")

# Fast Solution
start_time = time.time()
bisquares_fast = {}
for i in range(0, 251):
    for j in range(0, 251):
        k = i * i + j * j
        bisquares_fast[k] = 1
end_time = time.time()
print("Fast Solution")
print(
    f"Answer: {len(bisquares_fast.keys())} Time: {end_time-start_time} seconds."
)
