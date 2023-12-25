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


if today() == "Sunday":
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= my_email,
            msg=f"Subject:{today()} Motivation\n\n{return_quotes()}")