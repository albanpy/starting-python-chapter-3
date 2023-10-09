#Age Classifier
ages=int(input("Enter person's age:"))
if ages<=1:
    print("The person is an infant")
elif ages>1 and ages<13:
    print("The person is a child")
elif ages>=13 and ages<20:
    print("The person is a teenager")
elif ages>=20:
    print("The person is a adult")