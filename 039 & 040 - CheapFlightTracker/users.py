import sheety

first_name = input("What is your FIRST name?\n").lower()
last_name = input("What is your LAST name?\n").lower()
email = input("What is your EMAIL?\n").lower()
email_confirm = input("Please type your EMAIL again to confirm:\n").lower()

while email != email_confirm:
    email_confirm = input("Please type your EMAIL again to confirm:\n").lower()
data = {"user": {"firstName": first_name, "lastName": last_name, "email": email}}
print(f'Welcome, {first_name} {last_name} - {email}')
sheety.insert_data(data)
