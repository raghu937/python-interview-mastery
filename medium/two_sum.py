def two_sum(lst,target):
    seen = {}
    for index,i in enumerate(lst):
        missing_number = target - i

        if missing_number in seen:
            return f"found it {missing_number} + {i} and index of missing number is {seen[missing_number]} and index of a number is {index}"
        else:
            seen[i] = index
    
print(two_sum([1,2,3,4,5,6],9))
