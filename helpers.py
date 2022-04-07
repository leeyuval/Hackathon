username_input = """
MDTextField:
    hint_text: "Enter your company name"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.7}
    size_hint_x:None
    width:300
"""

phone_num_input = """
MDTextField:
    hint_text: "Enter  your phone number"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "phone"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    width:300
"""

address_input = """
MDTextField:
    hint_text: "Enter your address"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "home"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""

#
# def customer_info(self):
#     self.theme_cls.primary_palette = "Green"
#     screen = Screen()
#     self.customer_name = Builder.load_string(helpers.username_input)
#     self.phone_num = Builder.load_string(helpers.phone_num_input)
#     self.address = Builder.load_string(helpers.address_input)
#     button = MDRaisedButton(text='Done',
#                             pos_hint={'center_x': 0.5, 'center_y': 0.4},
#                             on_press=self.customer_data)
#     screen.add_widget(self.customer_name)
#     screen.add_widget(self.phone_num)
#     screen.add_widget(self.address)
#     screen.add_widget(button)
#     return screen

#     def customer_data(self, obj):
#         new_customer = Customer(self.customer_name.text, self.phone_num.text,
#                            self.address.text)
#
# if __name__ == '__main__':
#     App().run()
