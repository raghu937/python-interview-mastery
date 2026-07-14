def second_largest_number(lst):
    unique = sorted(set(lst)) 
    return unique[-2] if len(lst) >= 2 else None
print(second_largest_number([2,3,5,1,3,8,6,9]))
