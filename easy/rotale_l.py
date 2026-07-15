def rotate_list(lst,index_value):
    return lst[index_value:]+lst[:index_value]
print(rotate_list([1,2,3,4,5],2))