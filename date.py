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
        if not is_valid_date(day ,month,year):
            exit()
        for i in range(month-1):
            days_year += days_of_month[i]
            # print(days_year)
        days_year+=day
        return days_year
    
    def day_in_year(year):
        if is_leap(year):
            return 366
        else:
            return 365
    def date_diff(date_start,date_end):
        day_start,month_start,year_start = [int(e) for e in (date_start.split('-'))]
        day_end,month_end,year_end = [int(e) for e in (date_end.split('-'))]
        # print("date_start")
        # print(day_of_year(day_start,month_start,year_start))
        # print("date_end")
        # print(day_of_year(day_end,month_end,year_end))
        # print(day_of_year(day_end - day_start , month_end-month_start,year_end - year_start))
        date_diff = 0
        # print("burrito")
        # print(2 - abs(day_of_year(day_end,month_end,year_end) - day_of_year(day_start,month_start,year_start)))
        # print(date_diff)
        for i in range(year_start,year_end):
            # print("sandwich")
            date_diff+=day_in_year(i)
            # print(date_diff)
        date_diff -= day_of_year(day_start,month_start,year_start) - 1
        # print(date_diff)
        date_diff += day_of_year(day_end,month_end,year_end)
        # print(date_diff)
        # print(day_of_year(day_start,month_start,year_start))
        if date_diff < 0:
            exit()
        else:
            return date_diff
    
    def is_valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year):
            days[1] = 29
        if day < 1 or day > days[month - 1]:
            return False
        return True
    
    print(day_of_year(1, 12, 2025))
    print(date_diff("25-12-1999", "9-3-2000"))
except:
    print("Invalid")