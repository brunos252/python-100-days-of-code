"""
Email motivational quote on Monday
"""
import smtplib
import datetime as dt
import random

my_email = "*****@gmail.com"
password = "******"

now = dt.datetime.now()

if now.weekday() == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="bruno.sacaric@gmail.com",
                        msg="Subject:Motivation of the week\n\n" + random.choice(quotes))
    connection.close()
