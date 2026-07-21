def missing_number(lis,n):
    logic = n*(n+1)//2
    print(logic)
    print(sum(lis))
    missing_number = logic - sum(lis)
    return missing_number
print(missing_number([1,2,3,5,6],6))
