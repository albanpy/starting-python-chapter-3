#Shipping Charges
weight_package=float(input("Enter the weight of a package:"))
if weight_package<=2:
    ship_charge=weight_package*1.5
elif weight_package>2 and weight_package<=6:
    ship_charge=weight_package*3
elif weight_package>6 and weight_package<=10:
    ship_charge=weight_package*4
elif weight_package>10:
    ship_charge=weight_package*4.75
print(f"Weight of package of {weight_package} pounds charges ${ship_charge:,.2f} ")