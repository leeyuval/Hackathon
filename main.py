from customer import Customer

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import helpers
from kivy.lang import Builder


class App(MDApp):
    def build(self):
        return Sign.customer_info()

    def customer_info(self):
        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        self.customer_name = Builder.load_string(helpers.username_input)
        self.phone_num = Builder.load_string(helpers.phone_num_input)
        self.address = Builder.load_string(helpers.address_input)
        button = MDRaisedButton(text='Done',
                                pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                on_press=self.customer_data)
        screen.add_widget(self.customer_name)
        screen.add_widget(self.phone_num)
        screen.add_widget(self.address)
        screen.add_widget(button)
        return screen

    def customer_data(self, obj):
        new_customer = Customer(self.customer_name.text, self.phone_num.text,
                           self.address.text)

if __name__ == '__main__':
    App().run()
