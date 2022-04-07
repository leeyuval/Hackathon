from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen


class UserBoard(MDApp):
    def build(self):
        screen = Screen()
        label1 = MDRectangleFlatButton(
            text='Choose the dish you are interested in:',
            pos_hint={"center_x": .5, 'center_y': 0.9}, size_hint=(None, None),
            size=(30, 30),
            width=(5),
            text_color=(0 / 255, 51 / 255, 153 / 255, 1),
            line_color=(0, 0, 0, 0), font_size="40sp")
        filter = MDRectangleFlatButton(text='click for filter:',
                                       pos_hint={'center_x': 0.2,
                                                 'center_y': 0.8}, text_color=(
            0 / 255, 51 / 255, 153 / 255, 1), line_color=(0, 0, 0, 0),
                                       font_size="20sp")
        bnt1 = MDRectangleFlatButton(text='KOSHER',
                                     pos_hint={'center_x': 0.4,
                                               'center_y': 0.8})
        bnt2 = MDRectangleFlatButton(text='VEGI',
                                     pos_hint={'center_x': 0.55,
                                               'center_y': 0.8})
        bnt3 = MDRectangleFlatButton(text='B3',
                                     pos_hint={'center_x': 0.7,
                                               'center_y': 0.8})
        screen.add_widget(filter)
        screen.add_widget(bnt1)
        screen.add_widget(bnt2)
        screen.add_widget(bnt3)
        screen.add_widget(label1)
        return screen

if __name__ == '__main__':
    UserBoard().run()