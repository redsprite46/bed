#!/usr/bin/python3
# encoding: utf-8

from twilio.rest import TwilioRestClient
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate


class TwilioWrapper:
    def __init__(self):
        account_sid = 'AC28977f0feb2e950a79a55ad506134036'
        auth_token = '52a55a819e39d1ea062c0e6747790c37'
        self.client_ = TwilioRestClient(account_sid, auth_token)

    def call_phone(self, message_id):
        base_url = 'https://dl.dropboxusercontent.com/u/1054283/'
        base_url += 'bedmonitoring/voice/'

        message_url = base_url + message_id + '.xml'
        call = self.client_.calls.create(
            url=message_url,
            to='+819082323271',
            from_='+815031873167')
        print(call.sid)

    def send_sms(self, message_id):
        script = ''
        if message_id == 'moving':
            script = 'Bさんが離床行動中です。'
        elif message_id == 'left':
            script = 'Bさんが離床しました。'

        message = self.client_.messages.create(body=script,
                to="+819082323271",
                from_="+19094742681")
        print(message.sid)

    def send_email(self, message_id):
        subject = ''
        text = ''
        if message_id == 'moving':
            subject = 'Bさんが離床行動中です。'
            text = 'Bさんが離床行動中です。'
        elif message_id == 'left':
            subject = 'Bさんが離床しました。'
            text = 'Bさんが離床しました。'

        from_address = 'bedmonitoring2016@gmail.com'
        to_address = 'k.nakasho@gmail.com'

        msg = MIMEText(text)
        msg["Subject"] = subject
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Date"] = formatdate(localtime=True)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.set_debuglevel(True)
        smtp.login(from_address, 'scope-akita')

        smtp.send_message(msg)
        smtp.quit()

if __name__ == "__main__":
    my_twilio = TwilioWrapper()
    my_twilio.send_email('moving')