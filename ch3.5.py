mass=float(input("Enter an object's mass:"))
weight=mass*9.8
print(f'Weight={weight:,.2f} newtons')
if weight>500:
    print("Object is too heavy")
elif weight<100:
    print("Object is too light")