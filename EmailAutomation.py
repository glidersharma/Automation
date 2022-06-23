
import requests
import smtplib
import pandas as pd
import cred
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''


senderemail = cred.email
senderpassword = cred.password
recivermail = cred.toemail
recivername = cred.names
Server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
Server.ehlo()
Server.login(senderemail, senderpassword)



msg = MIMEMultipart()
for i in range(len(recivermail)):
    # msg.add_header('Content-Disposition', 'attachment', filename='empty.txt')
    msg['Subject'] = 'Sample Email for you' + ' ' + \
        str(now.day) + '-' + str(now.month) + '-' + str(now.year)+ str(now.time)
    msg['From'] = senderemail
    msg['To'] = recivermail[i]
    content +=(f'<br><br>Hey {recivername[i]} This is a sample email this service can be automated 100 times a day on you email address and can have ay typr of content \U0001F923<br><br>')        
    content = '<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://www.rd.com/wp-content/uploads/2019/09/GettyImages-621924830-scaled.jpg" width="592" height="422">'
    msg.attach(MIMEText(content, 'html'))
    print(recivermail[i])
    Server.sendmail(senderemail, recivermail[i], msg.as_string())

# print(Emaildetails[name]);


Server.close()
