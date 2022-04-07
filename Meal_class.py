class Meal:
    """
    expiration_date =
    labels =
    amount =
    """

    def __init__(self, dish_name, expiration_date, amount,is_kosher:bool,restaurant):
        self.dish_name = dish_name
        self.expiration_date = expiration_date
        self.amount = amount
        self.is_kosher = is_kosher
        self.restaurant = restaurant



    def set_expiration_date(self, new_exp):
        """
        edit or set the expiration date of a meal
        :param new_exp:
        :return:
        """
        self.expiration_date = new_exp

    def set_amount(self, new_amount):
        """

        :param new_amount:
        :return:
        """
        self.amount = new_amount

    def set_labels(self, new_labels: dict):
        """

        :param new_labels:
        :return:
        """
        self.labels = new_labels
