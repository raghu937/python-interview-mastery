def leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
print(leap_year(2028))

print("To find the leap year just add year")