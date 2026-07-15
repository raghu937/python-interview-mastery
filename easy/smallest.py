def smallest(lst):
    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    return smallest
print(smallest([1,2,3,4,5,6]))
