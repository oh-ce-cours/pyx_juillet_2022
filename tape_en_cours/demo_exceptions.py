import sys
import os

# from https://docs.python.org/3/library/email.examples.html
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(message)

# me == the sender's email address
# you == the recipient's email address
msg["Subject"] = f"Everything is broken, pleaz help"
msg["From"] = error @ example.com
msg["To"] = admin @ example.com

# Send the message via our own SMTP server.
s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()


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
