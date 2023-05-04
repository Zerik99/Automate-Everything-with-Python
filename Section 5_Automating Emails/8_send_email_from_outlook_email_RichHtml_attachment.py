import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Fake email info. Would use os.environ.get() to get real email info.
sender = "example.email@hotmail.com"
senderpw = "examplepassword"
receiver = "receiver.email@hotmail.com"

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "This is a Test Email"

body = """\
    <h1>This is Erik!</h1>
    <p>Just wanted to say hello!</p>
    """

mimetext = MIMEText(body, "html")
message.attach(mimetext)
message_text = message.as_string()

attachment_path = "Section 5_Automating Emails/files/Text.txt"
attachment_file = open(attachment_path, "rb")
payload = MIMEBase("application", "octate-stream")
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment", filename=attachment_path)
message.attach(payload)


server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, senderpw)
server.sendmail(sender, receiver, message_text)
server.quit()

print(message_text)
