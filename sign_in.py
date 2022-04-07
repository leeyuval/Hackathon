import kivy
import json
from kivy import uix

class SignIn:
    def __init__(self, output_stream, input_stream=None):
        self.type = None
        self.name = None
        self.username = None
        self.address = None
        self.phone = None
        self.users = {}
        if input_stream is not None:
            users = open(input_stream, "r")
            self.users = json.load(users)
            users.close()
        self.output_stream = output_stream

    def start(self):
        while True:
            self.username = input("Please enter your username: ")
            if self.username in self.users:
                self.password = input("Please enter your password: ")
                if self.password == self.users[self.username]["password"]:
                    self.set_user()
                    print("Welcome, " + self.name + "!")
                    return True
                else:
                    print("Incorrect Password")
                    continue
            else:
                self.set_name()
                self.set_address()
                self.set_phone()
                self.set_type()
                self.users[self.username] = {"type": self.type, "name": self.name, "address": self.address, "phone": self.phone}
                self.save()
                return True

    def set_user(self):
        self.type = self.users[self.username]["type"]
        self.name = self.users[self.username]["name"]
        self.address = self.users[self.username]["address"]
        self.phone = self.users[self.username]["phone"]

    def get_name(self):
        return self.users[self.username]["name"]

    def get_address(self):
        return self.users[self.username]["address"]

    def get_phone(self):
        return self.users[self.username]["phone"]

    def get_type(self):
        return self.users[self.username]["type"]

    def get_username(self):
        return self.username

    def set_name(self):
        self.name = input("Please enter your name: ")
        self.users[self.username]["name"] = self.name
        self.save()

    def set_address(self):
        self.address = input("Please enter your address: ")
        self.users[self.username]["address"] = self.address
        self.save()

    def set_phone(self):
        self.phone = input("Please enter your phone number: ")
        self.users[self.username]["phone"] = self.phone
        self.save()

    def set_type(self):
        self.type = input("Please enter student's type: ")
        self.users[self.username]["type"] = self.type
        self.save()


    def save(self):
        with open(self.output_stream, 'w') as outfile:
            json.dump(self.users, outfile)

class SignInScreen(uix.Screen):
    def __init__(self, **kwargs):
        super(SignInScreen, self).__init__(**kwargs)
        self.user = SignIn("users.json")
        self.sign_in.start()
        self.manager.current = "main"

