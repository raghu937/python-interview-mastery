def remove_duplicates(s):
    seen = set()
    result = []
    for i in s:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return ''.join(result)
print(remove_duplicates('mynameissuperstar'))