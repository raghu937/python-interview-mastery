def palindrome(word):
    return word == word[::-1]

print(palindrome('raghu'))
print(palindrome('racecar'))