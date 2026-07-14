def sum_of_digits(n):
    return sum(int(i) for i in str(abs(n)))
print(sum_of_digits(2026))

n = 1997
sum_value = 0
for i in str(n):
    sum_value += int(i)
print(sum_value)
