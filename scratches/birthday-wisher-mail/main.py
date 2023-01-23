# Extra Hard Starting Project

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
import smtplib

import pandas

data = pandas.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"].title())

    with smtplib.SMTP("smtp.freesmtpservers.com") as connection:
        # connection.starttls()
        # connection.login(user="email", password="password")
        connection.sendmail(
            from_addr="python@freesmtpservers.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
