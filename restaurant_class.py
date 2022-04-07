import kivy
from meal_class import Meal

class Restaurant:
    """
    location =
    opening hours =
    type =
    available_meals = array of Meal object
    """

    def __init__(self,name, location, opening_hours, f_type):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours
        self.f_type = f_type
        # self.av_meals = {}

    def set_location(self, new_location):
        """
        edit restaurant location
        :param new_location: address (str)
        :return: None
        """
        self.location = new_location

    def set_opening_hours(self, new_hours):
        """
        edit restaurant location
        :param new_hours: type str
        :return: None
        """
        self.opening_hours = new_hours

    # def add_meal(self, meal_obj, meal_name):
    #     """
    #     add an available meal object to the restaurant
    #     :param meal_name: str, type of meal
    #     :param meal_obj: Meal
    #     :return: None
    #     """
    #     self.av_meals[meal_name] = meal_obj

    #
    # def edit_meal(self, meal_name, amount, expiration_date,labels):
    #     """
    #
    #     :param meal_name:
    #     :param amount:
    #     :param expiration_date:
    #     :param labels:
    #     :return:
    #     """
    #     self.av_meals[meal_name].set_amount(amount)
    #     self.av_meals[meal_name].set_expiration_date(expiration_date)
    #     self.av_meals[meal_name].set_labels(labels)



