from collections import Counter
lis = ['hello', 'this', 'is', 'great','hello']

def count_occurence(lis):
    counts = Counter(lis)
    return counts
print(count_occurence(lis))


count_dict = {}

def number_of_count(lis):
    count = 0
    for i in lis:
        if i not in count_dict:
            count = 1
            count_dict[i] = count
        else:
            count_dict[i] += 1
    return count_dict
print(number_of_count(lis))



