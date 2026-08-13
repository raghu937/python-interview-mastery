nums = [1,2,3,4,5,11,13,12,6,7,2,2,2,2,8,9]
nums.append(10)
print(nums)
nums.remove(10)
print(nums)
nums.pop(0)
print(nums)
print(nums.index(2))
print(nums)
nums.sort()
print(nums)
print(len(nums))
x = sum(nums)/len(nums)
print(max(nums),min(nums),sum(nums),'average:',x,len(nums))

animals = ['tiger','lion','cheetah','bear','monkey','elephant',2,5]

print(animals.insert(8,'honey badger'))

print(set(nums) | set(animals))
print(set(nums) & set(animals))
print(animals)
nums.sort(reverse=True)
print(nums)
print(sorted(nums))

print(nums)
nums.reverse()
print(nums)

exists = 5 in nums
print(exists)

count_of_2 = nums.count(2)
print(count_of_2)

numericals = [4,4,5,6,7,8]
print(nums+animals)
print(nums)


#deep copy and shallow copy

import copy 
number_list = [[1,2,3],[4,5,6],[7]]
shallow = copy.copy(number_list)
shallow[0].append(100)
shallow.append(1922)

print(shallow)
print(number_list)

deep_copy = copy.deepcopy(number_list)
deep_copy[0].append(1000)
print(number_list)
print(deep_copy)

#In shallow copy , when nested lists are updated then it affects the original nested objects or data structure ,unless its updated on surface level. In deep copy , It doesn't affect the original structure of the object.

print(set(nums))

l1,l2 = [1,2,3],[3,4,5]
print(list[set(l1)&set(l2)])
print(list[set(l1)|set(l2)])
print(list[set(l1)-set(l2)])

new_flatten_list = [j  for i in number_list for j in i]
print(new_flatten_list)

def splitting_list(new_flatten_list,n):
    return [new_flatten_list[i:i+n] for i in range(0,len(new_flatten_list),n)]
print(splitting_list(new_flatten_list,3))

print(new_flatten_list)
def rotate(new_flatten_list,n):
    return new_flatten_list[n:] + new_flatten_list[:n]
print(rotate(new_flatten_list,4))

#second largest value in a list 

def second_largest(new_flatten_list):
    new_flatten_list.sort(reverse=True)
    return new_flatten_list[1]
print(second_largest(new_flatten_list))

#replace first and last

def replacing(new_flatten_list):
    print(new_flatten_list)
    new_flatten_list[0],new_flatten_list[-1] = new_flatten_list[-1],new_flatten_list[0]
    
    return new_flatten_list
print(replacing(new_flatten_list))

def count_even_odd(new_flatten_list):
    return sum(1 for i in new_flatten_list if i%2 ==0) , sum(1 for i in new_flatten_list if i%2 != 0)
print(count_even_odd(new_flatten_list))