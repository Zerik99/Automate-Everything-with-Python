import yagmail
import os
from time import sleep

sender = os.environ.get("Py_Automation_Gmail")
senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
receiver = os.environ.get("Personal_Gmail")

subject = "This is a Test Email"

contents = """Here is the body of my email."""

while True:
    yag = yagmail.SMTP(sender, senderpw)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    sleep(30)
