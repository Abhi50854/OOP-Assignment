
# Base class for all superheroes
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} from {self.city}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}.")

    def travel(self, vehicle):
        print(f"{self.name} is traveling.")
        vehicle.move()

# Subclass for heroes who can fly
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.flying_speed = flying_speed

    # Override use_power for flying heroes
    def use_power(self):
        print(f"{self.name} flies at {self.flying_speed} km/h and uses {self.power}.")

# Base class for vehicles
class Vehicle:
    def move(self):
        print("Vehicle is moving.")

# Different types of vehicles
class Car(Vehicle):
    def move(self):
        print("Car is driving.")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying.")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing.")

# Example usage
if __name__ == "__main__":
    # Create superhero objects
    hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
    hero2 = FlyingHero("Sky Blazer", "Laser Beams", "Metropolis", 300)

    # Create vehicle objects
    car = Car()
    plane = Plane()
    boat = Boat()

    # Use superhero methods
    hero1.introduce()      # Introduce hero1
    hero1.use_power()      # hero1 uses power
    hero1.travel(car)      # hero1 travels by car

    print("---")

    hero2.introduce()      # Introduce hero2
    hero2.use_power()      # hero2 uses power (overridden)
    hero2.travel(plane)    # hero2 travels by plane
    hero2.travel(boat)     # hero2 travels by boat
