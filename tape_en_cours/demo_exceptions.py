def f():
        1 / 0

def g():
    f()

try:
    g()
except Ex:
    pass 

