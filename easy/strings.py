#reverse a string or palindrome
def revers(s):
    s = s.lower()
    return s == s[::-1]
print(revers('Racecar'))
print(revers('party'))

#count of vowels and consonants

def vow_conso(s):
    vowels = 'aeiouAEIOU'
    count_of_vowels = sum(1 for i in s if i in vowels)
    count_of_consonants = sum(1 for i in s if i not in vowels)
    return count_of_vowels, count_of_consonants
print(vow_conso('Raghu'))

#count words in a sentence 

def count_of_words(s):
    return len(s.split())
print(count_of_words('My name is khan'))

#anagram
def anagram(a,b):
    return sorted(a.lower()) == sorted(b.lower())
print(anagram('listen','silent'))
print(anagram('karadi','kardibi'))

#remove all whitespaces

def remove_spaces():
    s = 'a b c'
    
    return s.replace(" ",'')
print(remove_spaces())

#replace word
def replacing_word():
    s = 'hello world'
    return s.replace('world','there')
print(replacing_word())

#join with separator


def join_list(lst):
    return '-'.join(lst)
print(join_list(['a','b','c','d']))

#count occurence of a character
def count_occurence(s,character):
    return s.count(character)
print(count_occurence('My name is Khan','a'))

#check digits
# def check_digits(s):
#      s = s.isdigit()
#      return 
# print(check_digits('123'))

is_digit = "12345".isdigit()
print(is_digit)
print('12345'.startswith('1'))
print('12345'.endswith('5'))