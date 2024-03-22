class Fruit:
    def __init__(self, name, price,color):
        self.name = name
        self.price = price
        self.color = color
Fruit1 = Fruit('Banana', 100, 'yellow')
Fruit2 = Fruit('Apple', 300, 'red')
Fruit3 = Fruit('Pear', 400, 'green')
Fruit4 = Fruit('Mango', 500, 'yellow')
Fruit5 = Fruit('Pineapple', 600, 'green')
print(f'{Fruit1.name} goes at an affordable price of {Fruit1.price}')
print(f'{Fruit2.name} is my favorite fruit of {Fruit2.color}')
print(f'{Fruit3.name} has a specific color of {Fruit3.color}')
print(f'{Fruit4.name} makes a tasty fruit juice and goes at {Fruit4.price} when blended with {Fruit1.name}')
print(f'{Fruit5.name} is Jannice favorite fruit')