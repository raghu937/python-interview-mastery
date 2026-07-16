def has_common(lst1,lst2):
    return bool(set(lst1)&set(lst2))

print(has_common([1,2,3],[4,5,6]))