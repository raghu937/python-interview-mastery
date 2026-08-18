def character_frequency(s):
    new_dict = {}
    count = 0
    for i in s:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    return max(new_dict.items(),key= lambda x:x[1])
        
print(character_frequency('aaabbbbccccccde'))