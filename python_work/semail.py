import smtplib
from email.mime.text import MIMEText

mail_host = '103.55.174.40'

mail_user = 'no_reply'

mail_pass = 'QqDZz.ZtgamE.2016&%)0111'

sender = 'no_reply@battleofballs.net'

receivers = ['297240222@qq.com']

message = MIMEText('content', 'plain', 'utf-8')

message['Subject'] = 'title'

message['From'] = sender

message['To'] = receivers[0]

try:
    smtpObj = smtplib.SMTP()

    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)

    smtpObj.sendmail(
        sender, receivers, message.as_string())

    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error', e)
