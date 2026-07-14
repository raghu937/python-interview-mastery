from collections import Counter

def occurences_count(s):
    return dict(Counter(s))
print(occurences_count('chandrashekara kambara'))

s = 'chandrashekara kambara'

count = 1
result = []
seen = {}
for i in range(len(s)):
    if s[i] in result:
        seen[s[i]] += count
    else:
        result.append(s[i])
        seen[s[i]] = count
print(seen)


    




