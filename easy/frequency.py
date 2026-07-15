from collections import Counter
def frequency_count(lst):
    print(Counter(lst).most_common(1)[0][0],Counter(lst).most_common(1)[0]) #first most common element and first common element count
    print(Counter(lst).most_common(2)[1][0]) #second most common element
    print(Counter(lst).most_common(3)[2][0]) #third most common element
    return 'Done'
print(frequency_count([1,1,2,2,2,2,4,3]))

def count(lst):
    seen = {}
    count = 0
    max_count = 0
    max_count_key = 0
    for i in lst:
        if i not in seen:
            seen[i] = 1
        elif i in seen:
            seen[i] +=1
    for x,y in seen.items():
        if y > max_count:
            max_count = y
            max_count_key = x
    

    return seen, f"most common element is :{max_count_key} with count of :{max_count}"
print(count([1,1,2,3,2,4,4,4]))