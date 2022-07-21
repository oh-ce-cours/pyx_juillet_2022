from exo1 import regle_fizz_buzz, est_divisible_par

# print("dans test_fizzbuzz.py", __name__)


def test_regles():
    assert regle_fizz_buzz(3) == "Fizz"
    assert regle_fizz_buzz(5) == "Buzz"
    assert regle_fizz_buzz(1) == "1"
    assert regle_fizz_buzz(15) == "FizzBuzz"

def divisibilite():
