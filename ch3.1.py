#Day of the Week
days=int(input("Enter a number in the range of 1 through 7 corresponding day of the week:"))
if days>=1 and days<=7:
    if days==1:
        print(f'{days}=Monday')
    elif days==2:
        print(f'{days}=Tuesday')
    elif days==3:
        print(f'{days}=Wednesday')
    elif days==4:
        print(f'{days}=Thursday')
    elif days==5:
        print(f'{days}=Friday')
    elif days==6:
        print(f'{days}=Saturday')
    else:
        print(f'{days}=Sunday')
else:
    print(f'{days} is out of range')