dictionary = {"a":1,"b":2}
print(dictionary)
print(list(dictionary))

dict_to_list = dictionary.items()
print(dict_to_list)
print(type(dict_to_list))
new_list = list(dict_to_list)
print(type(new_list))
print(type(new_list[0]))

#defaultdict : "if a key doesn't exist, automatically create it with this default value."
print(dictionary)

