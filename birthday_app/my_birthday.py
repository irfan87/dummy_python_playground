# this application is my datetime playground to get days of my next year birthday
import datetime

user_message = "Welcome user!"
user_message += "'\nPress 'q' or type 'quit' to terminate the application\n"
user_message += "\nPlease enter your birthday to count the days\n"

while True:
    current_date = datetime.date.today()
    user_response = input(user_message)

    if user_response == 'quit' or user_response == 'q':
        print('\nSee you again!')
        break
    
    user_birthday = datetime.datetime.strptime(user_response, '%d/%m/%Y').date()
    user_next_birthday = datetime.date(year=2021, month=6, day=15)
    birthday_days_left = user_next_birthday - current_date

    print(f"\nToday is {current_date.strftime('%d %b %Y')}\n")
    print(f"\nYour birthday is {user_birthday.strftime('%d %b %Y')}\n")
    print(f"\nYour next birthday is {birthday_days_left.days} days left\n")
    

