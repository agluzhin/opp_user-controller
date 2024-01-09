user_data = {}


class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        user_data[f'{self.name}'] = {
            'login': self.login, 'password': self.password}

    def log_in(self):
        print('Enter your login:')
        login = input()
        print('Enter your password:')
        password = input()

        if {'login': login, 'password': password} == user_data[f'{self.name}']:
            print(f'Hello, {self.name}. Access successfully gained!')
        else:
            print('Your personal data is incorrect. Access denied... Try again later.')

    def log_out(self):
        print(f'{self.name}, you are successfully exited.')

    def change_password(self):
        print('Enter new password:')
        password = input()
        user_data[f'{self.name}']['password'] = password
        print(f'{self.name}, your password is successfully changes.')


class Admin(User):
    def delete_user(self):
        print('Enter name of the user needed:')
        name = input()

        del user_data[name]

        print('User successfully deleted!')

    def create_user(self):
        print('Choose the new user name:')
        name = input()
        print('Choose the new user login:')
        login = input()
        print('Choose the new user pasword:')
        password = input()

        user_data[name] = {'login': login, 'password': password}

        print('User successfully created!')


class Guest(User):
    def show_personal_data(self):
        print(f'Your name is: {self.name}, your login: {
              self.login}, your password: {self.password}')


admin_user = Admin('Alex', 'northcat', 'dfksldfj1234')
guest_user = Guest('John', 'pipega', 'dfjla1294')
