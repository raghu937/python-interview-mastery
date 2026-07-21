def merged_sorted(a,b):
    i,j,merged = 0,0,[]
    while i < len(a) and j < len(b):

        merged.append(a[i])
        i += 1



        merged.append(b[j])
        j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    print(merged.extend(a[i:]))

    return sorted(merged)
print(merged_sorted([1,3,5,7,8],[2,4,6,9,10,11,12]))



# def merge_sorted(a, b):
#     i, j, merged = 0, 0, []
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             merged.append(a[i]); i += 1
#         else:
#             merged.append(b[j]); j += 1
#     merged.extend(a[i:])
#     merged.extend(b[j:])
#     return merged

# print(merge_sorted([1, 3, 5], [2, 4, 6]))