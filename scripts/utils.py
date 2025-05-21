import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

def send_email(recipient_email, sender_email, sender_password, attachment):
    msg = EmailMessage()
    msg['Subject'] = f"Automated Report - {datetime.now().strftime('%Y-%m-%d')}"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Email body
    msg.set_content(f"""
    Hello,

    Attached is the automated report for the day: {datetime.now().strftime('%Y-%m-%d')}.
    
    """)
    
    # Attachment
    with open(attachment, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image',
                                 subtype='png')

    # Try to send the email. On error, print the error
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    
    # Configure email settings
    recipient_email = os.environ.get("RECIPIENT_EMAIL")
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("EMAIL_PASSWORD")

    # Send the report via email
    send_email(recipient_email, sender_email, sender_password)