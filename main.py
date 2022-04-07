# from kivy.support import install_twisted_reactor
# from kivy.app import App
# from kivymd.app import MDApp
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
#
#
# class MainApp(App):
#     def build(self):
#         """getting info from user"""
#
#         # layout = GridLayout(cols=3)
#         name = TextInput(text='Enter your name')
#         phone_num = TextInput(text='Enter your phone number')
#         address = TextInput(text='Enter your address')
#         submit = Button(text='Submit',
#                         on_press=self.submit(name, phone_num, address))
#         # layout.add_widget(name)
#         # layout.add_widget(phone_num)
#         # layout.add_widget(address)
#         # layout.add_widget(submit)
#         return name
#
#     def submit(self, name, phone_num, address):
#         print(name.text, phone_num.text, address.text)
#
#
# if __name__ == '__main__':
#     MainApp().run()

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField

import helpers
from kivy.lang import Builder


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        screen = Screen()

        username = MDTextField(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint_x=None, width=200)

        username = Builder.load_string(helpers.username_input)
        screen.add_widget(username)
        print(username.text)
        return screen


DemoApp().run()