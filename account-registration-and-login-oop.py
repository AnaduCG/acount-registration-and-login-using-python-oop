class RegisterUser:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def registered(self):
        print(f"""User {self.name} successfuly created!
         Login now""")
        name2 = input('Enter your username: ')
        pass2 = input('Enter User password: ')
        if name2 == self.name and password == pass2:
            return f"User successfuly loged in as {name2}"
        else:
            return "invalid credentials!"


name = input('Register a username: ')
password = input('Create a password: ')

p1 = RegisterUser(name, password)
print(p1.registered())
