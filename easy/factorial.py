n = 5
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
print(factorial(n))


fac_output = 1

for i in range(n):
    fac_output = fac_output *(i+1)
print(fac_output)

