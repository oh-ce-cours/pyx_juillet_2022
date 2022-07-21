import random
import sys

random_number = random.randrange(1, 101)
input_number = -1
while input_number != random_number:
    try:
        input_number = int(input("Enter an integer number:"))
    except ValueError:
        print("Enter a number please")
        sys.exit(4)
        continue

    if input_number > random_number:
        print("Input Number is greater than random number")
    elif input_number < random_number:
        print("Input Number is less than random number")
print("Deal!!!")
