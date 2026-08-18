from collections import Counter
def count_non_repeating(s):

    count = Counter(s)
    for i in count:
        if count[i] == 1:
            print(i)
    return 'ok'

print(count_non_repeating('Raghuis a good boy'))



def count_of_strings(s):
    new_dict = {}
    for i in s:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    for i in new_dict:
        if new_dict[i] == 1:
            print(i,new_dict[i])
    return new_dict
print(count_of_strings('shahrukhkhan'))