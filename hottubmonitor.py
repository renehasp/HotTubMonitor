import smtplib
import os


IP = "192.168.1.149"
gmail_user = 'renehasp@gmail.com'
gmail_password = ''
sent_from = gmail_user
to = ['renehasp@gmail.com,9735727641@txt.att.net']
subject = '***WARNING**** Hot Tub breaker needs to be reset ***WARNING****'
body = 'Hot Tub breaker needs to be reset'



HOST_UP  = True if os.system("ping " + IP.strip(";")) is 0 else False

if HOST_UP == True:
    quit()
else:
    email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}
{body}
"""
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
       print("Something went wrong….", ex)