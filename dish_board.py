import pandas as pd
from Meal_class import Meal


class Dishes_Board:
    def __init__(self, filename):
        self.file = filename
        self.board = pd.read_csv(filename)


    def export_board(self):
        self.board.to_csv(self.file)


    def add_dish(self, dish: Meal):
        df_dish = {"dish name": dish.dish_name, "amount": dish.amount, "is kosher": dish.is_kosher,
                   "expiration date": dish.expiration_date,
                   "restaurant": dish.restaurant}
        self.board.append(df_dish)

    def get_dish_index(self, dish: Meal):
        cur_rest = dish.restaurant
        cur_dish_name = dish.dish_name
        dish_index = self.board.index[
            (self.board['dish name'] == cur_dish_name) | (self.board['restaurant'] == cur_rest)].tolist()

        return dish_index

    def update_amount(self, dish: Meal, new_amount: int):
        dish_index = self.get_dish_index(dish)
        self.board.at[dish_index, 'amount'] = new_amount

    def remove_dish_of_rest(self, dish: Meal):
        dish_index = self.get_dish_index(dish)
        self.board.drop(dish_index, inplace=True)





