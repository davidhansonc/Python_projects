import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from conf_template import message_html, message_text
from email_list import email_list


if __name__ == "__main__":
    sender = "churchintucson@gmail.com"
    receivers = list(email_list.values())
    password = input("Password: ")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Weekly Announcements"
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(message_text, "plain")
    part2 = MIMEText(message_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(
            sender, receivers, message.as_string()
        )