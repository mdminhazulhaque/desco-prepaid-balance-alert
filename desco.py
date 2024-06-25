#!/usr/bin/env python3

import os, sys
import smtplib, requests

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

DESCO_PREPAID_ACCOUNT_ID = os.getenv('DESCO_PREPAID_ACCOUNT_ID')
DESCO_PREPAID_USER_EMAIL = os.getenv('DESCO_PREPAID_USER_EMAIL')

SMTP_FROM_EMAIL = os.getenv('SMTP_FROM_EMAIL')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

# get balance from desco prepaid api
respose = requests.get("https://prepaid.desco.org.bd/api/tkdes/customer/getBalance?accountNo=" + DESCO_PREPAID_ACCOUNT_ID, verify=False)
balance = respose.json()['data']['balance']

# compose mail
msg = MIMEMultipart()
msg['From'] = SMTP_FROM_EMAIL
msg['To'] = DESCO_PREPAID_USER_EMAIL
msg['Subject'] = "Desco Prepaid Balance: {} Tk".format(balance)

body = """
Desco Prepaid Balance: {} Tk

""".format(balance)

msg.attach(MIMEText(body, 'plain'))

# fire
server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.ehlo()
server.starttls()
server.login(SMTP_USER, SMTP_PASSWORD)
server.sendmail(SMTP_FROM_EMAIL, DESCO_PREPAID_USER_EMAIL, msg.as_string())
