''' a simple employee class'''

class Employee:
    def __init__(self, first_name, last_name, age, work_title, is_working):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.work_title = work_title
        self.is_working = is_working

    def fullname(self):
        fullname = f'{self.first_name} {self.last_name}'
        
        return fullname.title()

    def user_email_address(self):
        joined_name = self.first_name + '.' + self.last_name
        name_no_whitespace = joined_name.replace(' ', '')
        email = f'{name_no_whitespace}@company.com'

        return email

    def user_info(self):
        if self.is_working:
            return f'\nName: {self.fullname()}\nAge: {self.age}\nWork Title: {self.work_title}\nEmail Address: {self.user_email_address()}'
        else:
            return f'\nName: {self.fullname()}\nAge: {self.age}\nWork Title: Not Working\nEmail Address: {self.user_email_address()}'

emp_1 = Employee(first_name='ahmad irfan', last_name='mohammad shukri', age=33, work_title='Software Developer', is_working=True)
print(emp_1.user_info())

