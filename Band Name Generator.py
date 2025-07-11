print("---------------Welcome to Band Name Generator---------------")
name=input("Enter your Name->")
print(f"Hii!" + name)

user_grewup_place=input(f"Enter the name of place where you grew up->")
print(user_grewup_place+f" is an nice place.")

user_pet_name=input("Enter the name of Pet you have or had before(if you never have or had pet please fill 'NONE')->")
if user_pet_name in ["NONE","none","no","na","NO","NA","None","No"]:
    print("Ok")
    print(f"Your Brand name could be-> ", user_grewup_place +" "+ name)
else:
    print(f"Your Brand name could be-> ",user_grewup_place +" "+ user_pet_name)
