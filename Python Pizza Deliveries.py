print("Welcome to Python Pizza Deliveries!")

size = input("What Size of Pizza do you want(S, M, L)? ").lower()
pepperoni = input("Do you want Pepperoni on your Pizza(Y or N)? ").lower()
extra_cheese = input("Do you want extra chees on your Pizza(Y or N)? ").lower()

bill = 0

if size=="s":
    print("Your Small Pizza is of $15")
    bill = 15
    if pepperoni=="y":
        bill += 2
        print("By adding Pepperoni your pizza is now of ", bill)
    elif pepperoni=="n":
        print("Okey")

    if extra_cheese=="y":
        bill += 1
        print("By adding Extra Chees your pizza is now of ", bill)
    elif extra_cheese=="n":
        print("Okey")

elif size=="m":
    print("Your Medium Pizza is of $20")
    bill = 20
    if pepperoni=="y":
        bill += 3
        print("By adding Pepperoni your pizza is now of ",bill)
    elif pepperoni=="n":
        print("Okey")

    if extra_cheese=="y":
        bill += 1
        print("By adding Extra Chees your pizza is now of ",bill)
    elif extra_cheese=="n":
        print("Okey")

elif size=="l":
    print("Your Large Pizza is of $25")
    bill = 25
    if pepperoni=="y":
        bill += 3
        print("By adding Pepperoni your pizza is no of ",bill)
    elif pepperoni=="n":
        print("Okey")
    
    if extra_cheese=="y":
        bill += 1
        print("By adding Extra Chees your pizza is now of ",bill)
    elif extra_cheese=="n":
        print("Okey")

else:
    print("Invalid Option Please try again!!!")

print("Your total bill is: ",bill)

