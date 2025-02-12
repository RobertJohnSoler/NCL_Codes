import smtplib

smtp_server = "smtp.mailtrap.io"
port = 2525
username = "your_mailtrap_username"
password = "your_mailtrap_password"

sender_email = "it-support@gatech.edu"
receiver_email = "ta@gatech.edu"
message = """From: IT Support <it-support@gatech.edu>
To: TA <ta@gatech.edu>
Subject: Urgent Security Alert

Dear student,

We detected unusual login attempts from your Georgia Tech account.
Please verify your credentials here: https://gatech-secure-login.com

- Georgia Tech IT Helpdesk
"""

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(username, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()