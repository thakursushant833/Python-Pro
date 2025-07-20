def my_function(number):
    return [x**2 for x in number]

print("Enter any 6 Number's in the List to do Square of each Numbers-> ")
number = [int(input("Number1= ")), int(input("Number2= ")), int(input("Number3= ")), int(input("Number4= ")), int(input("Number5= ")), int(input("Number6= "))]
print("Squares of the numbers are:", my_function(number))

