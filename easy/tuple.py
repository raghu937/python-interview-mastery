def create_tuple():
    s = ('a',1,4,'d')
    try:
        s[2] = 3
    except TypeError as e:
        print('Tuples are immutable:',e)
    return s[3]
print(create_tuple())


new_t = (('a',1),('b',2),('c',3))
a,b,c = new_t
print(a[0])
print(b[1])
print(c)

print(tuple(list(new_t)))

print(len(new_t))

new_b = (('d',4),('e',5),('f',6))
print(new_t + new_b)

a = (1,)
b = (2,)
print(a+b)
print(type(a))

print(('a',1) in new_t)
print('a' in  new_t[0])

occurence = (1,2,3,4,5,6,1,1,1,3,3,5,5)
print(occurence.count(5))
print(occurence.index(5))

for x,y in new_t:
    print(type(x),type(y))

print(max(occurence))
print(min(occurence))

print(max(new_b , key=lambda new_b:new_b[1]))


print(sorted(occurence))


pairs = [(1,3), (2,1), (3,2)]

pairs.sort(key=lambda x:x[0])
print(pairs)


d = {"a":1, "b":2}
print(type(d))
print(type(d.items()))
print(d.items())
print(list(d.items()))
print(d.values())
print(d.keys())