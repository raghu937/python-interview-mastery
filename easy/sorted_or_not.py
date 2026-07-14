def sorted_or_not(s):
    result = []
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            result.append('True')
        else:
            result.append('False')
    if 'False' in result:
        return False
    else:
        return True
print(sorted_or_not([1,2,3,4,5,2]))