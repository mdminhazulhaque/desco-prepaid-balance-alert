#!/usr/bin/env python3

import smtplib, ssl, requests
import os

DESCO_PREPAID_ACCOUNT_ID = os.getenv('DESCO_PREPAID_ACCOUNT_ID')
DESCO_PREPAID_USER_EMAIL = os.getenv('DESCO_PREPAID_USER_EMAIL')

SMTP_FROM_EMAIL = os.getenv('SMTP_FROM_EMAIL')
SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
SMTP_USER = os.getenv('SMTP_USER')

respose = requests.get("https://prepaid.desco.org.bd/api/tkdes/customer/getBalance?accountNo=" + DESCO_PREPAID_ACCOUNT_ID, verify=False)

balance = respose.json()['data']['balance']

message = F"""\
Subject: Desco Prepaid Balance {balance} Tk

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
    server.ehlo()
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_FROM_EMAIL, DESCO_PREPAID_USER_EMAIL, message)
