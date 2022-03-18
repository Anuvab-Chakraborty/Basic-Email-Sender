import smtplib
import ssl
from email.message import EmailMessage

subject="Email From PYTHON"
body="This is a test mail from Python !!"
sender_email="xyz@gmail.com"
reciever_email="zyx@gmail.com"
password=input("Enter a password: ")

message=EmailMessage()
message["From"]=sender_email
message["To"]=reciever_email
message["Subject"]=subject
#message.set_content(body)

html=f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html,subtype="html")

conteext=ssl.create_default_context()

print("Sending Email!!!")
#465 is a smtp port code that is used to access the ssl
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=conteext) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,reciever_email,message.as_string())

print("SUCCESS!!!")
