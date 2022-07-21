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


if __name__ == "__main__":
    # si la variable __name__ (gérée par l'interpréteur) est __main__ (si le fichier est appelé directement par l'interpréteur)
    fizzbuzz(100)
