def power_set(lst):
    result = [[]]
    for item in lst:
        result += [subset + [item] for subset in result]
    return result

print(power_set([1, 2, 3]))