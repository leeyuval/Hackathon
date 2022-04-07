import pandas as pd
from meal_class import Meal


class DishesBoard:
    def __init__(self, filename):
        self.file = filename
        self.board = pd.read_csv(filename)

    def export_board(self):
        self.board.to_csv(self.file, index=False)

    def add_dish(self, dish: Meal):
        df_dish = [{"dish name": dish.dish_name, "restaurant": dish.restaurant,
                    "expiration date": dish.expiration_date,
                    "amount": dish.amount, "is kosher": dish.is_kosher}]
        self.board = self.board.append(df_dish, ignore_index=True)

    def get_dish_index(self, dish: Meal):
        cur_dish_name = dish.dish_name
        cur_rest = dish.restaurant
        dish_index = self.board.index[
            (self.board['dish name'] == cur_dish_name) | (
                    self.board['restaurant'] == cur_rest)].tolist()

        return dish_index

    def update_amount(self, dish: Meal, new_amount: int):
        dish_index = self.get_dish_index(dish)
        self.board.at[dish_index, 'amount'] = new_amount

    def remove_dish_of_rest(self, dish: Meal):
        dish_index = self.get_dish_index(dish)
        self.board.drop(dish_index, inplace=True)


def main():
    dishes_board = DishesBoard("/Users/eitanmoed/Hackathon 2022/Hackathon/Dishes_Database.csv")
    print(dishes_board.board)
    # for col in dishes_board.board.columns:
    #     print(col)
    # hamburger = Meal("hamburger", 40, 20, True, "BBB")
    # sushi = Meal("sushi", 50, 40, False, "Hasushia")
    # salad = Meal("salad", 30, 10, True, "greeniz")
    # dishes_board.add_dish(hamburger)
    # dishes_board.add_dish(sushi)
    # dishes_board.add_dish(salad)
    # dishes_board.remove_dish_of_rest(hamburger)
    # dishes_board.update_amount(sushi, 20)
    # dishes_board.export_board()
    # print("after changes=", dishes_board.board)
    # print("Done editing")


if __name__ == "__main__":
    main()
