import random
import sys

random_number = random.randrange(1, 101)
input_number = -1
while input_number != random_number:
    try:
        input_number = nt(input("Enter an integer number:"))
    except ValueError:
        print("Enter a number please")
        sys.exit(6)
    except NameError:
        sys.exit(7)
        continue
    if input_number > random_number:
        print("Input Number is greater than random number")
    elif input_number < random_number:
        print("Input Number is less than random number")
print("Deal!!!")
