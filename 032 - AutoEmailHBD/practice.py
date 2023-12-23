import smtplib
import random
import datetime as dt

my_email = "musnik52coding@gmail.com"
my_password = "mxoh lypu mhxe syqy"
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 5: #saturday
    with open(r'032 - AutoEmailHBD\quotes.txt', 'r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # SECURITY ENCODING!
        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs="musnik52work@gmail.com",
            msg=f"Subject:QUOTES\n\n{quote}",
        )



