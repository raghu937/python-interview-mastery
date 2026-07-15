def hcf(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b // hcf(a,b)

print(lcm(4,6))