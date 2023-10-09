# Color Mixer
color1=str(input("Enter first primary color in small letters:"))
color2=str(input("Enter second primary collr in small letters:"))
if (color1=="red" or color1=="blue" or color1=="yellow") and (color2=="red" or color2=="blue" or color2=="yellow"):
    if(color1=="red" and color2=="blue") or (color1=="blue" and color2=="red"):
        print(f'{color1}+{color2}=purple')
    elif(color1=="red" and color2=="yellow") or (color1=="yellow" and color2=="red"):
        print(f'{color1}+{color2}=orange')
    elif(color1=="blue" and color2=="yellow") or (color1=="yellow" and color2=="blue"):
        print(f'{color1}+{color2}=green')
else:
    print("please enter only primary color")