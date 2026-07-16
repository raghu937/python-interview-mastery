def rotate_list(lst,value):
    return lst[value:]+lst[:value]
print(rotate_list([1,2,3,4,5,6],2))