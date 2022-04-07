import kivy
import json
from kivy import uix

class SignIn:
    def __init__(self, output_stream, input_stream=None):
        self.users = {}
        if input_stream is not None:
            users = open(input_stream, "r")
            self.users = json.load(users)
            users.close()
        self.output_stream = output_stream

    def set_username(self, username):
        self.users[username] = {}

    def set_password(self, username, password):
        self.users[username]["password"] = password

    def set_email(self, username, email):
        self.users[username]["email"] = email

    def get_name(self, username):
        return self.users[username]["name"]

    def get_address(self, username):
        return self.users[username]["address"]

    def get_phone(self, username):
        return self.users[username]["phone"]

    def get_type(self, username):
        return self.users[username]["type"]

    def set_type(self, username, type):
        self.users[username]["type"] = type

    def set_name(self, username, name):
        self.users[username]["name"] = name

    def set_address(self, username, address):
        self.users[username]["address"] = address

    def set_phone(self, username, phone):
        self.users[username]["phone"] = phone

    def save(self):
        with open(self.output_stream, 'w') as outfile:
            json.dump(self.users, outfile)


