def my_function(number):
    total = 0
    for num in number:
        if num % 2 == 0:
            total += num
    return total
print("Enter 6 numbers->")
print(my_function([(input("Number1=")), int(input("Number2=")), int(input("Number3=")), int(input("Number4=")), int(input("Number5=")), int(input("Number6="))]))
