word = 'ixi'
def palindrome(word):
    return word == word[::-1]
print(palindrome(word))


new_word_str = ''
for i in range(len(word)-1,-1,-1):
    new_word_str += word[i]
print(new_word_str==word)

