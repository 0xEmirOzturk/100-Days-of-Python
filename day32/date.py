import smtplib
import random
import datetime as dt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_email = []
password = []


def return_quotes():
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
    return random.choice(quotes_list)


def today():
    global days
    now = dt.datetime.now()
    day = now.weekday()
    return days[day]

today = today()
quote = return_quotes()

print(quote)