def duplicates(lst):
    seen = set()
    result = []
    duplicates = []
    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
        else:
            duplicates.append(i)
    return f"original list :{seen} and duplicates : {duplicates} "
print(duplicates([3,4,5,2,4,6,2,3]))