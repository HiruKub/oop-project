try:
    days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    def is_leap(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False
    def day_of_year(day, month ,year):
        days_year = 0
        if is_leap(year):
            days_of_month[1] = 29
        else:
            if (month == 2 and days_of_month[1] == 29) or (month == 2 and day >= 29):
                # days_of_month[1] = 28
                exit()
        if month > 12 or month < 1 or day < 1 or day > 31 or day > days_of_month[month-1]:
            exit()
        for i in range(month-1):
            days_year += days_of_month[i]
            # print(days_year)
        days_year+=day
        return days_year

    print(day_of_year(1, 12, 2025))
except:
    print("Invalid")