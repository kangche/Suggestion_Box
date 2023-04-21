import smtplib
from email.mime.text import MIMEText

import sys
sys.path.append('/root/Suggestion_Box')

from configure import config
def send_mail(html_message):
    msg = MIMEText(html_message, 'html')
    msg['From'] = config['mail']['login_mail']
    msg['To'] = config['mail']['to']
    msg['Subject'] = config['mail']['subject']
    smtp_server = config['mail']['smtp_server']
    smtp_port = config['mail']['smtp_port']
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # server.starttls()
        server.login(config['mail']['login_user'], config['mail']['login_pass'])
        text = msg.as_string()
        server.sendmail(config['mail']['login_mail'], [i.strip() for i in config['mail']['to'].split(',')], text)


if __name__ == '__main__':
    send_mail('<h>你们好</h>')
