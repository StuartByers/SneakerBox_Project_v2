class Sneaker:

    def __init__(self, model, brand, price, image_url, listed = False, id = None):
        self.model = model
        self.brand = brand
        self.price = price
        self.image_url = image_url
        self.listed = listed
        self.id = id

    def mark_list(self):
        self.listed = True