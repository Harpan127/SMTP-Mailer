import smtplib
import imghdr
from email.message import EmailMessage

# Your mail and password

EMAIL_ADDRESS = "YOUR MAIL"
EMAIL_PASSWORD = "YOUR PASSWORD"

# Mail construction

msg = EmailMessage()
msg["Subject"] = "Hi"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "RECEIVER MAIL"
msg.set_content("Here's my cat!")

# Open attachment

with open("cat.jpg", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

# Add attachment (with the correct filetype and name)

msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

# Login and sent

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print("Successfully logged in...")

        smtp.send_message(msg)
        print("Mail sent!")


except smtplib.SMTPAuthenticationError:
    print("Failed to Authenticate")
