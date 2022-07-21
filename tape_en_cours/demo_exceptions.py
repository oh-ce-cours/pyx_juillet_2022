import sys
import os

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg["Subject"] = f"The contents of {textfile}"
msg["From"] = me
msg["To"] = you

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
