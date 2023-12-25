from datetime import datetime
import pandas
import random
import smtplib

EMAIL = []
PASSWORD = []

today = datetime.now()
today_tuple = (today.month, today.day)
letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    random_letter = random.choice(letter)
    with open(f"letter_templates/{random_letter}", "r") as letter_read:
        content = letter_read.read()
        modified_content = content.replace("[NAME]", person["name"])

    print(random_letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr= EMAIL ,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday!\n\n{modified_content}")