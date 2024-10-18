from pprint import pprint

class  Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop():
    name = 'products.txt'
    def get_products(self):
        with open(self.name, 'r') as file:
            a = file.read().strip().splitlines()
        return a

    def add(self, *products):
        existing_products = self.get_products()
        with open(self.name, "a") as file:
            for a in products:
                if a in existing_products:
                    print(f"Продукт {a} уже есть в магазине")
                else:
                    file.write(f"\n{a}")

pop = Product("apple", 56, "vegetable")
com = Shop()
com.add(pop)
d = open("products.txt")
pprint(d.read())
com.add("яблоко", "груша")
pprint(d.read())





