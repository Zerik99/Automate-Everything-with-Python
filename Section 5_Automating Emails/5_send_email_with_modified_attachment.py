import yagmail
import os
import pandas


def send_emails(contactsdf: pandas.DataFrame, yagconnection: yagmail.SMTP):
    for index, col in contactsdf.iterrows():
        invoicefilename = f"{str(col['name']).replace(' ', '_')}.txt"
        receiver = col["email"]
        subject = "This is a Test Email"
        contents = [
            f"""Hello {col['name']}, You owe ${col['amountdue']}.""",
            f"Section 5_Automating Emails/files/invoices/{invoicefilename}",
        ]

        create_new_invoice(filename=invoicefilename, filecontent=str(contents[0]))

        yagconnection.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")


def create_new_invoice(filename: str, filecontent: str):
    with open(f"Section 5_Automating Emails/files/invoices/{filename}", "w") as f:
        f.write(filecontent)


def main():
    sender = os.environ.get("Py_Automation_Gmail")
    senderpw = os.environ.get("Py_Automation_Gmail_App_Pw")
    # receiver = os.environ.get("Personal_Gmail")
    yag = yagmail.SMTP(sender, senderpw)

    df = pandas.read_csv("Section 5_Automating Emails/files/EmailsWithAttach.csv")
    # print(df)

    send_emails(df, yag)


if __name__ == "__main__":
    main()
