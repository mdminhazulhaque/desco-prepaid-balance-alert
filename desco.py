#!/usr/bin/env python3

import smtplib, ssl, requests
import os

DESCO_PREPAID_ACCOUNT_ID = os.getenv('DESCO_PREPAID_ACCOUNT_ID')

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

respose = requests.get("http://prepaid.desco.org.bd/api/tkdes/customer/getBalance?accountNo=" + DESCO_PREPAID_ACCOUNT_ID)

balance = respose.json()['data']['balance']

message = F"""\
Subject: Desco Prepaid Balance {balance} Tk

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USER, EMAIL_USER, message)
