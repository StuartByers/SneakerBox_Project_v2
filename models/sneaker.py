class Sneaker:

    def __init__(self, model, user, price, listed = False,  id = None):
        self.model = model
        self.user = user
        self.price = price
        self.listed = listed
        self.id = id

    def mark_list(self):
        self.listed = True