def fib(n):
    seq = [0,1]
    while len(seq) < n:
        seq.append(seq[-2]+seq[-1])
    return seq[:n]
print(fib(5))