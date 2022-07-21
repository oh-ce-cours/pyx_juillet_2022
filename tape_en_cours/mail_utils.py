# from https://docs.python.org/3/library/email.examples.html
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage


def send_email(message):
    msg = EmailMessage()
    msg.set_content(message)

    msg["Subject"] = f"Everything is broken, pleaz help"
    msg["From"] = "error@example.com"
    msg["To"] = "admin@example.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP("localhost:1025")
    s.send_message(msg)
    s.quit()
