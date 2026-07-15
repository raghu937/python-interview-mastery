def armstrong_number(n):
    digits = str(n)
    length_of_number = len(digits)
    power = length_of_number
    return n == sum(int(i)**power for i in digits)
print(armstrong_number(153))