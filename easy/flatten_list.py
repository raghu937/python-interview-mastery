def flatten_list(lst):
    result = []
    for i in lst:
        if isinstance(i,list):
            result.extend(i)
        else:
            result.append(i)
    return result
print(flatten_list([[1],[1,2,3],[4,5],[5],{5}]))
