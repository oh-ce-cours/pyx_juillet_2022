import sys
import os


def f():
    1 / 0


def g():
    f()


try:
    g()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(
        f"L'exception {exc_type.__name__} s'est produite dans le fichier {fname} à la ligne {exc_tb.tb_lineno} avec pour message {str(e)}"
    )
