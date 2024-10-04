def date(day_number,year):
    days_months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year%4==0 and year%100!=0) or (year%400==0):
            days_months[1]=29
    month = 0
    while day_number > days_months[month]:
        day_number-= days_months[month]
        month += 1
    months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    print(day_number,months[month],year)
day_number=int(input("enter a day number:"))
year=int(input("enter the year:"))
date(day_number,year)
