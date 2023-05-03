import yagmail
import os
import pandas


sender = os.environ.get("Py_Automation_Gmail")
senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
receiver = os.environ.get("Personal_Gmail")
subject = "This is a Test Email"


yag = yagmail.SMTP(sender, senderpw)

df = pandas.read_csv("Section 5_Automating Emails/files/Emails.csv")
print(df)

for index, col in df.iterrows():
    print(col["email"])
    contents = f"""Hello {col['name']} Here is the body of my email."""
    yag.send(to=col["email"], subject=subject, contents=contents)
    print("Email Sent!")

# yag.send(to=receiver, subject=subject, contents=contents)
# print("Email Sent!")
