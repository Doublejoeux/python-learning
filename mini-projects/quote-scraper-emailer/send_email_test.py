from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText 

load_dotenv()  # reads the .env file and loads its values into the environment

gmail_address = os.getenv("GMAIL_ADDRESS")
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")

# Quick sanity check — don't print the actual password, just confirm it loaded
if gmail_address and gmail_app_password:
    print("Credentials loaded successfully.")
else:
    print("Missing credentials — check your .env file.")

# Build the email
subject = "Another test email from Python"
body = "If you're reading this, just know that smtplib works and you're doing great."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = gmail_address
msg["To"] = gmail_address # sending to self for the test

# Connect and send
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # upgrades the connecction to encrypted (TLS)
        server.login(gmail_address, gmail_app_password)
        server.send_message(msg)
        print("Email sent successfully.")
except smtplib.SMTPAuthenticationError as e:
    print(f"Login failed — {e}.")
except Exception as e:
    print(f"Something went wrong: {e}")
