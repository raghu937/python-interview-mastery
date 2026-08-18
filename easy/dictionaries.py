dictionary = {}
dictionary['Kavya'] = 35
dictionary['Nandan'] = 31
dictionary['Raghu'] = 29
dictionary['Ravi'] = 33

print(dictionary)
#dictionary.get(key, default)
print(dictionary.get('Raghu',0))
print(dictionary.get('Raghu'))
print(dictionary.get('Raghu',1))
print(dictionary.get('Chandrashekar',0))

print(dictionary)
# print(dictionary.pop('Raghu'))
print(dictionary)

# del dictionary['Ravi']
print(dictionary)

#pop() → remove + return value
#del   → remove only

d2 = {"a":1, "b":2}

new_dict = {**dictionary,**d2}
print(new_dict)

print(max(new_dict.items(),key= lambda x:x[1]))
print(min(new_dict.items(),key= lambda x:x[1]))
print(max(new_dict,key=new_dict.get))
print(min(new_dict,key=new_dict.get))


sorted_dict = sorted(new_dict.items(),key = lambda x:x[1])
print(type(sorted_dict))
print(sorted_dict)




lst = [1,2,3,4,5,1,1,1,2,2,3,4,5,5]
def count_of_repeated(lst):
    seen = {}
    for i in lst:
        seen[i] = seen.get(i,0)+1
    return seen, max(seen.items() ,key=lambda x:x[1])
print(count_of_repeated(lst))

#inverting dictionary

print(new_dict)
inverted_dict = {y:x for x,y in new_dict.items()}
print(inverted_dict)

keys = ["a","b","c"]
vals = [1,2,3]

x = zip(keys,vals)
print(type(x))
print(dict(x))

trignometry = ((1,2),(3,4),(5,6))
print(type(trignometry))
x = dict(trignometry)
print(type(x))