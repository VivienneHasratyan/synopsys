class Crepe:
    def __init__(self, base_type, fillings, toppings, fold_style, extras):
        self.base_type = base_type
        self.fillings = fillings
        self.toppings = toppings
        self.fold_style = fold_style
        self.extras = extras

    def __str__(self):
        return (f"Crepe ({self.base_type} base)\n"
                f"Fillings: {', '.join(self.fillings)}\n"
                f"Toppings: {', '.join(self.toppingss) if self.toppingss else 'None'}\n"
                f"Fold Style: {self.fold_style}\n"
                f"Extra: {', '.join(self.extras) if self.extras else 'None'}")


class CrepeBuilder:
        def __init__(self):
            self.reset()

        def reset(self):
            self.crepe = Crepe(None, [], [], None, [])

        def set_base_type(self): pass
        def add_fillings(self): pass
        def add_toppings(self): pass
        def add_fold_style(self): pass
        def add_extras(self): pass

        def build(self):
            return self.crepe

class CrepeSuzetteBuilder(CrepeBuilder):
    def set_base_type(self):
        self.crepe.base_type = "sweet"

    def add_fillings(self):
        self.crepe.fillings = ["orange zest", "butter", "sugar"]

    def add_toppings(self):
        self.crepe.toppings = ["orange sauce"]

    def set_fold_style(self):
        self.crepe.fold_style = "triangle"

    def add_extras(self):
        self.crepe.extras = []

class SuperNutellaCrepeBuilder(CrepeBuilder):
    def set_base_type(self):
        self.crepe.base_type = "sweet"

    def add_fillings(self):
        self.crepe.fillings = ["Nutella", "strawberries", "bananas"]

    def add_toppings(self):
        self.crepe.toppings = ["whipped cream"]

    def set_fold_style(self):
        self.crepe.fold_style = "triangle"

    def add_extras(self):
        self.crepe.extras = ["Nutella"]

class SalmonHolidayCrepeBuilder(CrepeBuilder):
    def set_base_type(self):
        self.crepe.base_type = "savory"

    def add_fillings(self):
        self.crepe.fillings = ["creme cheese", "salmon", "avocado"]

    def add_toppings(self):
        self.crepe.toppings = ["olives"]

    def add_extras(self):
        self.crepe.extras = []

class CrepeDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_crepe(self):
        self._builder.reset()
        self._builder.set_base_type()
        self._builder.add_fillings()
        self._builder.add_toppings()
        self._builder.set_fold_style()
        self._builder.add_extras()
        return self._builder.build()

if __name__ == "__main__":
    director = CrepeDirector(CrepeSuzetteBuilder())
    crepe1 = director.construct_crepe()
    print("== Crêpe Suzette ==")
    print(crepe1)

    director = CrepeDirector(SuperNutellaCrepeBuilder())
    crepe1 = director.construct_crepe()
    print("== Super Nutella Crêpe ==")
    print(crepe1)

    director = CrepeDirector(SalmonHolidayCrepeBuilder())
    crepe1 = director.construct_crepe()
    print("== Salmon Holiday Crêpe ==")
    print(crepe1)