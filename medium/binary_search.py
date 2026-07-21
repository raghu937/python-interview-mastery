def binary_search(lst,target):
    lo,hi = 0, len(lst)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if lst[mid]==target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid -1
    return 'done'
print(binary_search([1,2,3,4,5,6,7,8],7))


