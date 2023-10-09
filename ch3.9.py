#Roulette Wheel Colors
num=int(input("Enter a pocket number:"))
if num>=0 and num<=36:
    if num==0:
        print(f"The pocket {num} is green")
    elif num>=1 and num<=10:
        if num%2==1:
          print(f"The pocket {num} is red")
        elif num%2==0:
            print(f"The pocket {num} is black")  
    elif num>=11 and num<=18:
        if num%2==1:
          print(f"The pocket {num} is black")
        elif num%2==0:
            print(f"The pocket {num} is red") 
    elif num>=19 and num<=28:
        if num%2==1:
          print(f"The pocket {num} is red")
        elif num%2==0:
            print(f"The pocket {num} is black") 
    elif num>=29 and num<=36:
        if num%2==1:
          print(f"The pocket {num} is black")
        elif num%2==0:
            print(f"The pocket {num} is red") 
else:
    print(f"{num} is outside the range of 0 through 36.")