def regle_fizz_buzz(nombre: int) -> str:
    res = ""
    if nombre % 3 == 0:
        res += "Fizz"
    if nombre % 5 == 0:
        res += "Buzz"

    if not res:
        res = str(nombre)

    return res


def fizzbuzz(nombre_max: int):
    for nombre in range(1, 1 + nombre_max):

        print(res)


fizzbuzz(100)