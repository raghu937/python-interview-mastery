def only_digits(s):
    return s.isdigit()
print(only_digits('123'))

def alpha_numeric(s):
    print(s.isalnum())
    return s.isalpha() 
print(alpha_numeric('as'))