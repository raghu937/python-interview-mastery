def anagram(a,b):
    return sorted(a.lower()) == sorted(b.lower())
print(anagram('silent','listen'))
print(anagram('python','jython'))