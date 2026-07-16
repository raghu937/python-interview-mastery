def check_start_end(word):
    return bool(word[0].lower()==word[-1].lower()) and len(word)>1

print(check_start_end('Level'))
print(check_start_end('Raghu'))
print(check_start_end('R'))