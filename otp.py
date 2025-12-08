import random
import smtplib
from email.message import EmailMessage
otp = ""
for i in range(6):
  otp+=str(random.randint(0,9))

from_mail = "sselvin308@gmail.com"
app_password = "hfgw gxxg tcxd mgjp"  

to_mail = input("Enter your email: ")

msg = EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content("Your OTP is: " + otp)

try:
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(from_mail, app_password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print("Error while sending email:", e)
    exit()

input_otp = input("Enter your OTP: ")
if input_otp == otp:
    print("OTP verified ✅")
else:
    print("Invalid OTP ❌")

print("Process Completed")