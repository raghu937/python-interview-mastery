def is_valid_parens(s):
    lis = []
    dict_pair = {')':'(',']':'[','}':'{'}

    for i in s:
        if i in '([{':
            lis.append(i)
            print(lis)
    
        elif i in dict_pair:
            if not lis or lis.pop() != dict_pair[i]:
                return False
    return not lis


print(is_valid_parens("(([]))]"))


# def is_valid_parens(s):
#     stack = []
#     pairs = {")": "(", "]": "[", "}": "{"}
#     for ch in s:
#         if ch in "([{":
#             stack.append(ch)
#         elif ch in pairs:
#             if not stack or stack.pop() != pairs[ch]:
#                 return False
#     return not stack

# print(is_valid_parens("{[()]}"))