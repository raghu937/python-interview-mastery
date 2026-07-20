def pair_sum(lst,target):
    seen = set()
    for i in lst:
        missing_value = target - i
        if missing_value in seen:
            print(f"{i}+{missing_value}")
        seen.add(i)
    return 'Done'
print(pair_sum([1,2,3,4,5,6,7,8],9))