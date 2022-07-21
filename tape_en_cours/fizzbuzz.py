def regle_fizz_buzz(nombre: int):
    res = ""
    if nombre % 3 == 0:
        res += "Fizz"
    if nombre % 5 == 0:
        res += "Buzz"

    if not res:
        res = str(nombre)
    print(res)


def fizzbuzz(nombre_max: int):
    for nombre in range(1, 1 + nombre_max):
        regle_fizz_buzz(nombre)


print(regle_fizz_buzz(1) == "1")
print(regle_fizz_buzz(3) == "Fizz")
print(regle_fizz_buzz(5) == "Buzz")
print(regle_fizz_buzz(15) == "FizzBuzz")
# fizzbuzz(100)
