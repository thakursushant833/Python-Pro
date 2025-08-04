print("Welcome to roler coster")

height=int(input ("What is your hight in cm? "))

bill = 0

if height > 120:
    print("You can ride the rolar coster")
    age=int(input("Enter your Age:"))

    if age<=12:
        print("Childrins Ticket's are $5")
        bill = 5

    elif 18>=age:
        print("Young's Ticket's are $7")
        bill = 7

    else:
        print("Adults Ticket's are $10")
        bill = 10
    
    photo=input("Do you want to have a photo taken? Type y for Yes and type n for No: ")

    if photo=="y":
        print(f"Your total bill is {bill}+3:",bill + 3)

    else:
        print(f"No Problam,Your total bill is {bill}:")     

else:
    print("You can not ride")