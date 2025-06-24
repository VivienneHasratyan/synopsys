import abc

# 1. --- Abstract Products ---
class Engine(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns engine's description"""

class Wheel(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns wheel's description"""

class Interior(abc.ABC):
    @abc.abstractmethod
    def get_description(self):
        """Returns interior's description"""

# 2. --- Concrete Products ---

# BMW Family components
class BMW_Engine(Engine):
    def get_description(self):
        return "BWM Engine"

class BMW_Wheel(Wheel):
    def get_description(self):
        return "BWM Wheel"

class BMW_Interior(Interior):
    def get_description(self):
        return "BWM Interior"

# Mini Family components
class Mini_Engine(Engine):
    def get_description(self):
        return "Mini Engine"

class Mini_Wheel(Wheel):
    def get_description(self):
        return "Mini Wheel"

class Mini_Interior(Interior):
    def get_description(self):
        return "Mini Interior"

# RollsRoyce Family components
class RollsRoyce_Engine(Engine):
    def get_description(self):
        return "RollsRoyce Engine"

class RollsRoyce_Wheel(Wheel):
    def get_description(self):
        return "RollsRoyce Wheel"

class RollsRoyce_Interior():
    def get_description(self):
        return "RollsRoyce Interior"

# 3. --- Abstract Factory ---
class CarComponentsFactory(abc.ABC):
    @abc.abstractmethod
    def create_engine(self):
        """Factory method to create engine for specific brand"""
        pass

    @abc.abstractmethod
    def create_wheel(self):
        """Factory method to create wheel for specific brand"""
        pass

    @abc.abstractmethod
    def create_interior(self):
        """Factory method to create interior for specific brand"""
        pass

# 4. --- Concrete Factories ---
class BMW_Factory(CarComponentsFactory):
    def create_engine(self):
        return BMW_Engine()

    def create_wheel(self):
        return BMW_Wheel()

    def create_interior(self):
        return BMW_Interior()

class Mini_Factory(CarComponentsFactory):
    def create_engine(self):
        return Mini_Engine()

    def create_wheel(self):
        return Mini_Wheel()

    def create_interior(self):
        return Mini_Interior()

class RollsRoyce_Factory(CarComponentsFactory):
    def create_engine(self):
        return RollsRoyce_Engine()

    def create_wheel(self):
        return RollsRoyce_Wheel()

    def create_interior(self):
        return RollsRoyce_Interior()


def run(factory: CarComponentsFactory):
    """Simulates assembling a car using components from a specific brand's factory."""
    brand_name = factory.__class__.__name__.replace('_Factory', '')
    print(f"\n--- Assembling a {brand_name} car ---")

    engine = factory.create_engine()
    wheel = factory.create_wheel()
    interior = factory.create_interior()

    print(f"  Engine:   {engine.get_description()}")
    print(f"  Wheels:   {wheel.get_description()}")
    print(f"  Interior: {interior.get_description()}")
    print("-------------------------------------------------")
# 5. --- Client Code ---

if __name__ == "__main__":
    print("Welcome to the BMW Group Car Assembly Configurator!")
    print("Choose a brand to assemble components for:")
    print("1. BMW")
    print("2. Mini")
    print("3. Rolls-Royce")

    choice = input("Enter number (1, 2, or 3): ").strip()

    chosen_factory: CarComponentsFactory = None

    if choice == "1":
        chosen_factory = BMW_Factory()
    elif choice == "2":
        chosen_factory = Mini_Factory()
    elif choice == "3":
        chosen_factory = RollsRoyce_Factory()
    else:
        print("Invalid choice. Please select a valid brand.")
        exit()

    run(chosen_factory)

    print("\nBMW Group car assembly simulation complete.")
