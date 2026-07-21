def max_value(s):
    max_value = 0
    for i in s:
        if i > max_value:
            max_value = i
    return max_value
print(max_value([1,2,3,4,6,8,5,9]))