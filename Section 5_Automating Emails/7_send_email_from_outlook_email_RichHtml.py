import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, senderpw)
server.sendmail(sender, receiver, message_text)
server.quit()

print(message_text)
