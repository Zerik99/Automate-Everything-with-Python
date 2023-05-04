import smtplib

# Fake email info
sender = "example.email@hotmail.com"
senderpw = "examplepassword"
receiver = "receiver.email@hotmail.com"

message = """\
    subject: This is a Test Email
    
    This is Erik!
    Just wanted to say hello!
    """

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, senderpw)
server.sendmail(sender, receiver, message)
server.quit()
