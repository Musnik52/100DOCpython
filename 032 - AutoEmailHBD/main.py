##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

from random import randint
import pandas
import smtplib
import datetime as dt

my_email = "musnik52coding@gmail.com"
my_password = "mxoh lypu mhxe syqy"

now = dt.datetime.now()
today_date = (now.day, now.month)

data = pandas.read_csv(r"032 - AutoEmailHBD\birthdays.csv")
birthday_dict = {(row["day"], row["month"]): row for (i, row) in data.iterrows()}


if today_date in birthday_dict:
    birthday_name = birthday_dict[today_date]["name"]
    birthday_email = birthday_dict[today_date]["email"]
    with open(
        f"032 - AutoEmailHBD\letter_templates\letter_{randint(1,3)}.txt", "r"
    ) as file:
        greeting = file.read()
        adjusted_greeting = greeting.replace("[NAME]", birthday_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # SECURITY ENCODING!
        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject:HAPPY BD!\n\n{adjusted_greeting}",
        )
