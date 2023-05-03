import yagmail
import os
import pandas

sender = os.environ.get("Py_Automation_Gmail")
senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
receiver = os.environ.get("Personal_Gmail")
yag = yagmail.SMTP(sender, senderpw)

subject = "This is a Test Email"

df = pandas.read_csv("Section 5_Automating Emails/files/EmailsWithAttach.csv")
# print(df)

for index, col in df.iterrows():
    contents = [
        f"""Hello {col['name']},  Here is the body of my email.""",
        f"{col['attachmentpath']}",
    ]
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
