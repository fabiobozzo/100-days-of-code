import random
import smtplib
import datetime as dt

my_email = "alice@freesmtpservers.com"

# connection = smtplib.SMTP("smtp.freesmtpservers.com")
# connection.starttls()
# connection.login(user=my_email, password="12345678")
# connection.close()

now = dt.datetime.now()
# print(now)
# print(now.month)
# if now.year == 2023:
#     print("Happy new year!")

# date_of_birth = dt.datetime(year=1988, month=6, day=22, hour=6)
# print(date_of_birth)

# -------------------------------------------------------------

dow = 0  # Monday
# dow = 6  # Sunday

try:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
except (FileNotFoundError, IOError) as err:
    print(f"failed to read quotes file: {err}")
    quotes = ["\"Fuck off!\" - Ricky LaFleur"]

if now.weekday() == dow:
    quote = random.choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.freesmtpservers.com") as connection:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bob@freesmtpservers.com",
            msg=f"Subject: Monday motivational quote\n\n{quote}"
        )
