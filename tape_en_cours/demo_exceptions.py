def f():
    1 / 0


def g():
    f()


try:
    g()
except Exception as e:
    print(e)
