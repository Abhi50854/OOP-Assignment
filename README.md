# 🦸 Superhero & Vehicle Program

This Python program demonstrates **Object-Oriented Programming (OOP)** concepts such as **classes, inheritance, method overriding, and polymorphism** using superheroes and vehicles.

## 🚀 Features

* **Superhero Base Class**

  * Each superhero has a name, power, and city.
  * They can introduce themselves, use their powers, and travel using different vehicles.

* **FlyingHero Subclass**

  * Inherits from `Superhero`.
  * Adds a new attribute `flying_speed`.
  * Overrides the `use_power()` method to include flying speed.

* **Vehicle Base Class**

  * Acts as a parent for all vehicles.
  * Contains a generic `move()` method.

* **Vehicle Subclasses**

  * `Car` → "Car is driving."
  * `Plane` → "Plane is flying."
  * `Boat` → "Boat is sailing."

* **Polymorphism in Action**

  * When a hero travels, the `vehicle.move()` method behaves differently depending on the type of vehicle.

## 📂 File Structure

```
superhero_program.py   # Main Python script
```

## ▶️ Example Usage

```python
# Create superhero objects
hero1 = Superhero("Shadow Knight", "Invisibility", "Gotham")
hero2 = FlyingHero("Sky Blazer", "Laser Beams", "Metropolis", 300)

# Create vehicles
car = Car()
plane = Plane()
boat = Boat()

# Hero actions
hero1.introduce()      # I am Shadow Knight from Gotham.
hero1.use_power()      # Shadow Knight uses Invisibility.
hero1.travel(car)      # Shadow Knight is traveling. Car is driving.

print("---")

hero2.introduce()      # I am Sky Blazer from Metropolis.
hero2.use_power()      # Sky Blazer flies at 300 km/h and uses Laser Beams.
hero2.travel(plane)    # Sky Blazer is traveling. Plane is flying.
hero2.travel(boat)     # Sky Blazer is traveling. Boat is sailing.
```

## 🧩 Concepts Learned

* **Encapsulation** → Keeping attributes inside classes.
* **Inheritance** → `FlyingHero` inherits from `Superhero`.
* **Polymorphism** → Different vehicles respond uniquely to `move()`.
* **Method Overriding** → `FlyingHero` overrides `use_power()`.

## 📌 How to Run

1. Save the code as `superhero_program.py`.
2. Run it using:

   ```bash
   python superhero_program.py
   ```
3. Watch the superheroes in action!
