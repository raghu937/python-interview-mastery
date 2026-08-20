#defaultdict : "if a key doesn't exist, automatically create it with this default value." "defaultdict is best at:Grouping — collecting multiple items under a shared key."


from collections import defaultdict
students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eve", "B"),
    ("Frank", "A"),
]

group = defaultdict(list)
count = defaultdict(int)
total = 1

for x,y in students:
    group[y].append(x)
    count[y] += total
print(group)
print(type(group))

print(count)
print(type(count))
print(dict(count))

print(students)

new_dict = {}

for x,y in students:
    new_dict.setdefault(y,[]).append(x)
print(new_dict)