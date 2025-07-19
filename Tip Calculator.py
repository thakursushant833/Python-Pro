print("----------Welcome to the tip Calculater!----------")
total_bill=int(input("What was the total bill? "))
tip=int(input("How much tip would you like to give?10,12 or 15? "))
while True:
    if tip >= total_bill:
        print("Not possible!! Please Enter Again")
        tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
        continue
    else:
        break
     
total_people = int(input("How many people to split the bill? "))
total_bill = total_bill + tip
each_person = total_bill / total_people
print("Each person should pay: ",round(each_person,2))