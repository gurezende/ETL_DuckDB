import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

def send_email(recipient_email, sender_email, sender_password, message, report_md, charts):
    """Send an email with a report as a markdown attachment and a chart as a PNG attachment.
    
    Parameters:
    recipient_email (str): The email address to send the report to.
    sender_email (str): The email address used to send the report.
    sender_password (str): The password for the sender email address.
    message (str): The body of the email.
    report_md (str): The path to the report file.
    charts (str): The path to the chart file.
    
    Returns:
    None
    
    Raises:
    Exception: If an error occurs when sending the email."""
    
    msg = EmailMessage()
    msg['Subject'] = f"Automated Report - {datetime.now().strftime('%Y-%m-%d')}"
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Email body
    msg.set_content(message)
    
    # Attachments
    msg.add_attachment(open(report_md, "rb").read(), maintype="text", subtype="markdown", filename="report.md")

    # Attach Charts
    for chart in charts:
        with open(chart, 'rb') as fp:
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