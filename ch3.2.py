# Areas of Rectangles
length1=float(input("Enter length of rectangle one:"))
length2=float(input("Enter length of rectangle two:"))
width1=float(input("Enter width of rectangle one:"))
width2=float(input("Enter width of rectangle two:"))
area1=length1*width1
area2=length2*width2
if area1>area2:
    print(f'Area of rectangle one={area1:,.2f}\nArea of rectangle two={area2:,.2f}\n'
    'Rectangle one has the greater area')
elif area2>area1:
    print(f'Area of rectangle one={area1:,.2f}\nArea of rectangle two={area2:,.2f}\n'
    'Rectangle Two has the greater area')
else:
    print(f'Area of rectangle one={area1:,.2f}\nArea of rectangle two={area2:,.2f}\n'
    'Areas of rectangles are the same')