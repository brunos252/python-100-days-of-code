"""
check closing prices of stock, if the change day-over-day is > 5%,
send top 3 news to email
"""

import requests
from datetime import datetime, timedelta
import smtplib
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
date_today = datetime.today().date()
date_yesterday = date_today - timedelta(days=1)
date_day_before = date_yesterday - timedelta(days=1)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=30min&apikey' \
      '=***** '
news_api_url = "https://newsapi.org/v2/everything"

news_api_key = "***"

MY_EMAIL = "*****@gmail.com"
MY_PASSWORD = "****"

response = requests.get(url=url)
data = response.json()
close_price_yesterday = float(data["Time Series (Daily)"][str(date_yesterday)]["4. close"])
close_price_day_before = float(data["Time Series (Daily)"][str(date_day_before)]["4. close"])

percentage_change = abs(close_price_yesterday - close_price_day_before) / close_price_day_before * 100

if percentage_change > 5:
    print("sending")
    news_parameters = {
        "q": COMPANY_NAME,
        "from": date_today,
        "sortBy": "popularity",
        "apiKey": news_api_key,
        "language": "en",
    }
    news_response = requests.get(url=news_api_url, params=news_parameters)
    news_data = news_response.json()
    articles = news_data["articles"][:3]

    if close_price_yesterday > close_price_day_before:
        header = f"{STOCK}: +{round(percentage_change, 2)}%"
    else:
        header = f"{STOCK}: -{round(percentage_change, 2)}%"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for i in range(3):
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="***@gmail.com",
                msg=f"Subject:{header}\n\ntitle:\n{html.unescape(articles[i]['title'])}\ndescription:\n{html.unescape(articles[i]['description'][:-3])}"
            )

