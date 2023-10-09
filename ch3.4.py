#Roman Numerals
num=int(input("Enter number within the range of 1 through 10:"))
if num>=1 and num<=10:
    if num==1:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "1\t\tI\n_____________________________")
    elif num==2:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "2\t\tII\n_____________________________")
    elif num==3:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "3\t\tIII\n_____________________________")
    elif num==4:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "4\t\tIV\n_____________________________")
    elif num==5:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "5\t\tV\n_____________________________")
    elif num==6:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "6\t\tVI\n_____________________________")
    elif num==7:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "7\t\tVII\n_____________________________")
    elif num==8:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "8\t\tVIII\n_____________________________")
    elif num==9:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "9\t\tIX\n_____________________________")
    elif num==10:
        print("_____________________________\nNumber\t\tRoman Numeral\n_____________________________\n"
        "10\t\tX\n_____________________________")

else:
    print(f'{num} is out of range')
