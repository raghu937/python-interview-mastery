def string_to_list(s):
    
    return s.split() ,'length:', len(max(s.split(),key=len)),max(s.split(),key=len)
print(string_to_list('raghu is a good boy'))