from collections import defaultdict

def group_anagrams(lst):
    dict_list = defaultdict(list)
    for words in lst:
        key = "".join(sorted(words))
        print(key)
        dict_list[key].append(words)
    return dict_list
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        