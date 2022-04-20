

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"


class Menu:
    def __init__(self):
        self.items = []

    def add(self, it):
        self.items.append(it)

    def remove(self):
        return self.items.pop()

    def iterator(self):
        return MenuIterator(self.items)


class MenuIterator:
    def __init__(self, items):
        self.index = 0
        self.items = items

    def has_next(self):
        return True if self.index < len(self.items) else False

    def next(self):
        it = self.items[self.index]
        self.index += 1
        return it


if __name__ == "__main__":
    item1 = FoodItem("Burger", 7)
    item2 = FoodItem("Pizza", 8)
    item3 = FoodItem("Chicken", 10)

    menu = Menu()
    menu.add(item1)
    menu.add(item2)
    menu.add(item3)

    print("-- Displaying Menu --")
    iterator = menu.iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)
