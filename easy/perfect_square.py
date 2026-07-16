def perfect_square(n):
    root = int(n**0.5)
    return root*root == n
print(perfect_square(49))
print(perfect_square(3))