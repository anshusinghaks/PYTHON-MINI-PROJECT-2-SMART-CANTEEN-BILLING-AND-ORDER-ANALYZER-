print("Welcome To Smart Canteen")
print("1.Veg Sandwich-Rs.60")
print("2.Masala Dosa-Rs.80")
print("3.Chole Rice-Rs.90")
print("4.Paneer Roll-Rs.100")
print("5.tea-Rs.20")

total=0
while True:
    choice=int(input("enter item number:"))
    quantity=int(input("enter a quantity:"))

    if quantity <=0:
        print("Please enter valid quantity:")
        continue
    if choice==1:
        name="Veg Sandwitch"
        price=60
    elif choice==2:
        name="Masala Dosa"
        price=80
    elif choice==3:
        name="Chole Rice"
        price=90
    elif choice==4:
        name=="Paneer Roll"
        price=100
    elif choice==5:
        name="Tea"
        price=20
    else:
        print("Invalid item number")
        continue  
    cost= price*quantity
    total=total+cost
    print(name,"X",quantity,"=",cost)

    print("Total Amount:",total)

    if total>=500:
        discount=total*10/100
    elif total>=250:
        discount=total*5/100
    else:
        discount=0

    final_amount=total-discount

    print("Discount:",discount)
    print("Final Amount:",final_amount)

    if total==0:
        print("No order ploaced")
    else:
        print("Thank you!")
    