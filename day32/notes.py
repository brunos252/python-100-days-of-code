# email SMTP, dateandtime module
# email with smtplib
import smtplib

my_email = "*****@gmail.com"
password = "******"

connection = smtplib.SMTP("smtp.gmail.com")
# make connection secure
connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="****@gmail.com", msg="Subject:Hello\n\nThis is the body")
connection.close()  # also possible: with smtplib.SMTP(...) as connection

# datetime
import datetime as dt

now = dt.datetime.now()
print(now)          # datetime type
print(now.year)     # int type
print(now.weekday())

date_of_birth = dt.datetime(year=1997, month=8, day=18, hour=10, minute=30)
print(date_of_birth)


# running the code in the cloud
# pythonanywhere - free account, possible to schedule 1 task daily
