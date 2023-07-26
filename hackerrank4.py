def is_leap(year):
    leapyear = False
    while 1900 < year and year < 10000 : 
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leapyear = True 
            return leapyear
            break 
        else : 
            return leapyear




year = int(input())
print(is_leap(year))