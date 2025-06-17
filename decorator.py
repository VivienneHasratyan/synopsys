class Coffee:
    def cost(self):
        return 5  # base price

    def description(self):
        return "Basic Coffee"

# Decorator base for coffee add-ons
class CoffeeAddon:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()

# Milk add-on
class Milk(CoffeeAddon):
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", Milk"

# Sugar add-on
class Sugar(CoffeeAddon):
    def cost(self):
        return self.coffee.cost() + 0.5

    def description(self):
        return self.coffee.description() + ", Sugar"

order = Coffee()
order = Milk(order)
order = Sugar(order)

print(order.description())
print("Total price: $", order.cost())