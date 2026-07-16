def index_of_list(lst,target):
    return [x for x,y in enumerate(lst) if y == target]
print(index_of_list([1,2,3,4,5,121,43,21],121))