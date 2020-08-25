''' a simple employee class'''

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)

emp_1.first_name = 'ahmad irfan'.title()
emp_1.last_name = 'mohammad shukri'.title()
emp_1.age = 33
emp_1.work_title = 'Python Software Developer'
emp_1.email_address = 'irfanshukri203@gmail.com'
emp_1.is_working = True

if emp_1.is_working:
    print(f'\nName: {emp_1.first_name} {emp_1.last_name}\nAge: {emp_1.age}\nWork Title: {emp_1.work_title}\nEmail Address: {emp_1.email_address}')
else:
    print(f'\nName: {emp_1.first_name} {emp_1.last_name}\nAge: {emp_1.age}\nWork Title: Not Working\nEmail Address: {emp_1.email_address}')