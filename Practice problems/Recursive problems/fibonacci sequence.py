
def find_nth_term(target_term):
    if target_term < 2:
        return 1     
    return find_nth_term(target_term-1) + find_nth_term(target_term-2)

x = int(input("What is the term you wish to find?: "))
print(find_nth_term(x))
