def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(3,5,2))

list = [2,3,5,1,3,6]
max_value = 0
for i in list:
    if i > max_value:
        max_value = i
print(max_value)