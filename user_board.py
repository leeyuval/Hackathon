from kivy.metrics import dp
from kivy.uix.togglebutton import ToggleButton
from kivymd.app import MDApp
import pandas as pd
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivy.uix.image import AsyncImage
from kivy.uix.stacklayout import StackLayout
from dish_board import DishesBoard
from kivy.uix.button import Button


class UserBoard(MDApp):
    def __init__(self):
        super(UserBoard, self).__init__()
        self.screen = Screen()

    def build(self):
        img = AsyncImage(
            source="https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/rm344-audi-04-a-x.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=9862deb301390ab373587cabfeb2a468")
        label1 = MDRectangleFlatButton(
            text='Choose the dish you are interested in:',
            pos_hint={"center_x": .5, 'center_y': 0.9}, size_hint=(None, None),
            size=(30, 30),
            width=(5),
            text_color=(0 / 255, 51 / 255, 153 / 255, 1),
            line_color=(0, 0, 0, 0), font_size="30sp")
        filter = MDRectangleFlatButton(text='click for filter:',
                                       pos_hint={'center_x': 0.2,
                                                 'center_y': 0.8}, text_color=(
                0 / 255, 51 / 255, 153 / 255, 1), line_color=(0, 0, 0, 0),
                                       font_size="20sp")
        bnt1 = MDRectangleFlatButton(text='Kosher',
                                     pos_hint={'center_x': 0.4,
                                               'center_y': 0.8})
        bnt2 = MDRectangleFlatButton(text='Vegi',
                                     pos_hint={'center_x': 0.55,
                                               'center_y': 0.8})
        bnt3 = MDRectangleFlatButton(text='Gluten free',
                                     pos_hint={'center_x': 0.70,
                                               'center_y': 0.8})

        self.screen.add_widget(img)
        self.screen.add_widget(filter)
        self.screen.add_widget(bnt1)
        self.screen.add_widget(bnt2)
        self.screen.add_widget(bnt3)
        self.screen.add_widget(label1)
        self.add_meals()
        return self.screen

    def add_meals(self):
        meals_board = DishesBoard(
            r"C:\Users\omerk\Desktop\Dishes_Database.csv").board.iterrows()
        i = 0
        j = 0
        for index, meal in meals_board:
            if str(meal['dish name']) != 'nan':
                b = Button(text=str(meal['dish name']) + '\n' + str(
                    meal['restaurant']) + '\n' + 'Amount:' + str(
                    int(meal['amount'])), pos_hint=(
                    {'center_x': 0.2 + i / 5, 'center_y': 0.6 - j / 5}),
                           size_hint=(None, None), size=(dp(100), dp(100)),
                           background_color=(0, 0, 0, 0.2),
                           bold=True, italic=True,
                           color=(0 / 255, 51 / 255, 153 / 255, 1))
                self.screen.add_widget(b)
                i = i + 1
            if i == 4:
                i = 0
                j = j + 1


class Board(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    UserBoard().run()
