def is_leap(year):
    leapYear = False
    while 1900 < year and year < 10000 : 
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leapYear = True 
            return leapYear
            break 
        else : 
            return leapYear




year = int(input())
print(is_leap(year))