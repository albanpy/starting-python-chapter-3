#Money Counting Game
#1 dollar=100cents, 1 penny=1 cent,1 nickel=5cents,1 dime=10 cents,1 quarter=25cents
penny=int(input("Enter number of pennies:"))
nickels=int(input("Enter number of nickels:"))
dimes=int(input("Enter number of dimes:"))
quarters=int(input("Enter number of quarters:"))
total=(penny*1)+(nickels*5)+(dimes*10)+(quarters*25)
if total==100: #this 100 cent of coins is equal to one dollar
    print(f'congratulations for winning a game!!')
elif total>100: #above one dollar
    print(f'Amount of {total} cents was more than one dollar')
elif total<100: #below one dollar
    print(f'Amount of {total} cents was less than one dollar')


