def regle_fizz_buzz(nombre: int) -> str:
    # fonction pure
    res = ""
    if nombre % 3 == 0:
        res += "Fizz"
    if nombre % 5 == 0:
        res += "Buzz"

    if not res:
        res = str(nombre)

    return res


def fizzbuzz(nombre_max: int):
    # fonction impure (ne retourne rien)
    for nombre in range(1, 1 + nombre_max):
        res = regle_fizz_buzz(nombre)
        print(res)


print("dans fizzbuzz.py", __name__)
# if est_lance_directement:
#     fizzbuzz(100)
