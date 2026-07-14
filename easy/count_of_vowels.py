def vowels(word):
    return sum(1 for i in word if i.lower() in 'aeiou')
print(vowels('why this kolaveri di:SONG'))