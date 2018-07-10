# https://automatetheboringstuff.com/chapter16/

"""
Python provides smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine
with an SMTP or ESMTP listener daemon.
"""

import smtplib

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    print(type(smtpObj))

    # Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server.
    smtpObj.ehlo()

    """
    If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to call the starttls() 
    method next. This required step enables encryption for your connection. If you are connecting to port 465 (using SSL), 
    then encryption is already set up, and you should skip this step.
    """
    smtpObj.starttls()

    sender_email = 'raunakshakya707@gmail.com'  # input("Enter your email id : ")
    password = 'naradevi12345'  # input("Enter password for your email id : ")
    receiver_email = 'rkshakya99@gmail.com'  # input("Whom do you want to send mail : ")
    subject = 'Greetings'  # input("What is the subject of the mail? ")
    message = 'Hello World!'  # input("Type the message : ")

    smtpObj.login(sender_email, password)

    """
    The start of the email body string must begin with 'Subject: \n' for the subject line of the email.
    The '\n' newline character separates the subject line from the main body of the email.
    """
    smtpObj.sendmail(sender_email, receiver_email, 'Subject: %s\n%s' % (subject, message))
    print("Successfully sent email")
    smtpObj.quit()
except Exception:
    print("Error: unable to send email")
