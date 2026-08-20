import copy

orig_d = {}

sample = [("a",1), ("a",2), ("b",3)]
dict_sample = dict(sample)
print(dict_sample)
orig_d = dict_sample
print(orig_d)
copy_d = orig_d.copy()
deep_copy= copy.deepcopy(orig_d)
print(copy_d)

copy_d['c'] = 4
print(orig_d)
print(copy_d)
print(deep_copy)


#shallow copy and deep copy concept same for list and dict but learned one more concept in dict , that is replacing a nested data structure will not affect the original data structure .
original_dict = {'name': 'Raghu', 'skills': {'Python': 3, 'FastAPI': 2}}
print(original_dict)
shallow_copy = original_dict.copy()
deep_copi = copy.deepcopy(original_dict)
print(shallow_copy)
shallow_copy['skills']['Python'] = 5
shallow_copy['skills']= {'java':4,'postgresql':4} #replacing nested data structure
print(original_dict)
print(shallow_copy)

deep_copi['skills']['Python'] = 10
deep_copi['skills'] = {'c++':8,'django':3}

print(original_dict)
print(deep_copi)