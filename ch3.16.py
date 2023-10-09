#February Days,leap year
year=int(input("Enter a year:"))
if(year%100)==0:
    if(year%400)==0:
        print(f'In {year} February has 29 days')
elif (year%100)!=0:
    if(year%4)==0:
        print(f'In {year} February has 29 days') 