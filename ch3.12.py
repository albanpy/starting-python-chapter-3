#Software Sales
pack1_cost=99
pack=float(input("Enter the number of packages purchased:"))
total_purchase=pack1_cost*pack
if pack>=10 and pack<=19:
    #total_purchase=pack1_cost*pack
    disc=total_purchase*0.1
    total_purchase_disc=total_purchase-disc
    print(f'Amount of Discount=${disc:,.2f}\n'
    f'Total amount of the purchase after the discount=${total_purchase_disc:,.2f}')
elif pack>=20 and pack<=49:
    #total_purchase=pack1_cost*pack
    disc=total_purchase*0.2
    total_purchase_disc=total_purchase-disc
    print(f'Amount of Discount=${disc:,.2f}\n'
    f'Total amount of the purchase after the discount=${total_purchase_disc:,.2f}')
elif pack>=50 and pack<=99:
   # total_purchase=pack1_cost*pack
    disc=total_purchase*0.3
    total_purchase_disc=total_purchase-disc
    print(f'Amount of Discount=${disc:,.2f}\n'
    f'Total amount of the purchase after the discount=${total_purchase_disc:,.2f}')
elif pack>=100:
    #total_purchase=pack1_cost*pack
    disc=total_purchase*0.4
    total_purchase_disc=total_purchase-disc
    print(f'Amount of Discount=${disc:,.2f}\n'
    f'Total amount of the purchase after the discount=${total_purchase_disc:,.2f}')
else:
    #total_purchase=pack1_cost*pack
    print(f'Total amount of the purchase=${total_purchase:,.2f}\n'
    f'There are no any discount for {pack} packages')
      
   
