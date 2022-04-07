import customer
import sign_in
import dish_board
import user_board

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager, Screen
import helpers
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    WelcomeScreen:
    SignInScreen:
    SignUpScreen:
    DishBoardScreen:


<WelcomeScreen>:
    name: 'welcome_screen'
    MDRectangleFlatButton:
        text: 'Sign In'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'sign_in'
    MDRectangleFlatButton:
        text: 'Sign Up'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'sign_up'

<SignInScreen>:
    name: 'sign_in'
    MDTextField:
        id: username
        hint_text: 'Username'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        icon_right: 'account-circle'
        on_text_validate: root.validate_username()
    MDTextField:
        id: password
        hint_text: 'Password'
        icon_right: 'eye-off'
        hint_text_mode: 'password'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'welcome_screen'
    
<SignUpScreen>:
    name: 'sign_up'
    MDTextField:
        id: username
        hint_text: 'Username'
        pos_hint: {'center_x':0.5,'center_y':0.9}
        icon_right: 'account-circle'
        on_text_validate: root.set_username()
    MDTextField:
        id: password
        hint_text: 'Password'
        icon_right: 'eye-off'
        hint_text_mode: 'password'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_text_validate: root.set_password()
    MDTextField:
        id: confirm_password
        hint_text: 'Confirm Password'
        icon_right: 'eye-off'
        hint_text_mode: 'password'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_text_validate: root.validate_confirm_password()
    MDTextField:
        id: email
        hint_text: 'Email'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        icon_right: 'email'
        on_text_validate: root.set_email()
    MDTextField:
        id: phone
        hint_text: 'Phone'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        icon_right: 'phone'
        on_text_validate: root.set_phone()
    MDTextField:
        id: address
        hint_text: 'Address'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        icon_right: 'location-on'
        on_text_validate: root.set_address()
    MDLabel:
        text: "Restaurant"
        halign: 'center'
        pos_hint: {'center_x':0.2,'center_y':0.23}
    MDCheckbox:
        id: Restaurant
        pos_hint: {'center_x':0.8,'center_y':0.23}
        
    MDRectangleFlatButton:
        text: 'Enter'
        pos_hint: {'center_x':0.4,'center_y':0.05}
        on_press: root.manager.current = 'dish_board'
    
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.6,'center_y':0.05}
        on_press: root.manager.current = 'welcome_screen'

<DishBoardScreen>:
    name: 'dish_board'
    on_enter: root.call_page()

"""


class WelcomeScreen(Screen):
    pass


class SignInScreen(Screen):
    def validate_username(self):
        if self.ids.username.text == 'admin':
            self.ids.username.error = 'Username is already taken'
        else:
            self.ids.username.error = ''


class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.username = ''
        self.flag = True
        self.flag1 = True

    def set_username(self):
        self.flag = False
        self.username = self.ids.username.text
        sign_in.set_username(self.ids.username.text)
        sign_in.save()

    def set_password(self):
        self.flag1 = False
        if self.flag:
            self.set_username()
        sign_in.set_password(self.username, self.ids.password.text)

    def validate_confirm_password(self):
        if self.flag1:
            self.set_password()
            sign_in.save()
        if self.ids.password.text != self.ids.confirm_password.text:
            self.ids.confirm_password.error = 'Passwords do not match'

    def set_email(self):
        if self.flag1:
            self.set_password()
        sign_in.set_email(self.username, self.ids.email.text)
        sign_in.save()

    def set_phone(self):
        if self.flag1:
            self.set_password()
        sign_in.set_phone(self.username, self.ids.phone.text)
        sign_in.save()

    def set_address(self):
        if self.flag1:
            self.set_password()
        sign_in.set_address(self.username, self.ids.address.text)
        sign_in.save()

    def set_type(self):
        if self.ids.Restaurant.active:
            sign_in.new_type = 'Restaurant'
        else:
            sign_in.new_type = 'Customer'
        sign_in.save()


class DishBoardScreen(Screen):
    def call_page(self):
        user_board.UserBoard().run()


sign_in = sign_in.SignIn("/Users/eitanmoed/Desktop/out.json", None)
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome_screen'))
sm.add_widget(SignInScreen(name='sign_in'))
sm.add_widget(SignUpScreen(name='sign_up'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


# class App(MDApp):
#     def build(self):
#
#         return self.customer_info()

# def customer_info(self):
#     self.theme_cls.primary_palette = "Green"
#     screen = Screen()
#     self.customer_name = Builder.load_string(helpers.username_input)
#     self.phone_num = Builder.load_string(helpers.phone_num_input)
#     self.address = Builder.load_string(helpers.address_input)
#     button = MDRaisedButton(text='Show',
#                             pos_hint={'center_x': 0.5, 'center_y': 0.4},
#                             on_press=self.show_data)
#     screen.add_widget(self.username)
#     screen.add_widget(self.phone_num)
#     screen.add_widget(self.address)
#     screen.add_widget(button)
#     return screen
#
# def show_data(self, obj):
#     new_cus = customer(self.username.text, self.phone_num.text,
#                        self.address.text)


if __name__ == '__main__':
    DemoApp().run()
