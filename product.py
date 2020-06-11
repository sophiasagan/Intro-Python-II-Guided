
class Product: #Parent Class / Base Class / Super Class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 10

    def __str__(self):
        return f'{self.name}: ${self.price} (great deal)'

class Sneaker(Product): #Child Class / Subclass / 
    def __init__(self, name, price, shoe_size, brand):
        #super returns the parent class instance
        super().__init__(name, price)
        self.shoe_size = shoe_size
        self.brand = brand

class SoccerBall(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def __str__(self):
        return f'{self.name}: ${self.price} WILSOOOOONNNNNNNNNN'

    def kick(self):
        print("The ball flew away")


generic_product = Product("Generic Thing", "99.99")
print(generic_product)
nike_free = Sneaker("Nike Free", "100", "10", "Nike")
print(nike_free)
soccer_ball = SoccerBall("Wilson","20", "Rubber")
print(soccer_ball)
soccer_ball.kick()

# print(nike_free.name)
# print(nike_free.price)
# print(nike_free.brand)
# print(soccer_ball.price)
# print(soccer_ball.discount)
# print(nike_free.discount)