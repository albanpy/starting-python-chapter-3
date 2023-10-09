# Magic Dates
day=int(input("Enter day in numeric form:"))
month=int(input("Enter month in numeric form:"))
year=int(input("Enter last two digit of a year:"))
if(day>=1 and day<=31) and (month>=1 and month<=12) and (year>=10 and year<=99):###validate day,month,year
    dates=day*month
    if dates==year:
        print(f'{day}/{month}/{year} is magic date')
    else:
        print(f'{day}/{month}/{year} is not magic date')
else:
    print("Enter day,month and year in guided ways")