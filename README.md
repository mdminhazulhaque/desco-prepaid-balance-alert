# Desco Prepaid Balance Alert

Get Desco Prepaid Balance delivered to your mailbox via CronJob/Schedule.

![Desco Prepaid Balance Checker](<diag.png>)

## Configure

Export the following variables.

```bash
export DESCO_PREPAID_ACCOUNT_ID=2233445566
export DESCO_PREPAID_USER_EMAIL=you@gmail.com
export SMTP_FROM_EMAIL=you@gmail.com
export SMTP_HOST=smtp.gmail.com
export SMTP_PASSWORD=apppasswordsimple
export SMTP_PORT=587
export SMTP_USER=you@gmail.com
```

Then run

```
python3 desco.py
```
