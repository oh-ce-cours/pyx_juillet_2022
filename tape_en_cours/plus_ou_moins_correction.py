import random

random_number = random.randrange(1, 101)
input_number = 0
while input_number != random_number:
    input_number = int(input("Enter an integer number:"))
    if input_number > random_number:
        print("Input Number is greater than random number")
    elif input_number < random_number:
        print("Input Number is less than random number")
print("Deal!!!")
