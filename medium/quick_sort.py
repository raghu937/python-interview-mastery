def quick_sort(lis):
    if len(lis) <= 1:
        return lis
    mid_value = lis[len(lis)//2]
    left_side = [i for i in lis if i < mid_value]
    middele_value = [i for i in lis if i == mid_value]
    right_side = [i for i in lis if i > mid_value]

    return quick_sort(left_side) + middele_value + quick_sort(right_side)

print(quick_sort([2,3,1,6,8,7,9]))


