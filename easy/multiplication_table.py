def tables(n):
    new_list = []
    for i in range(1,11):
        new_list.append(f"{n} * {i} = {n*i}")
    return "\n".join(new_list)
print(tables(5))
print(tables(12))