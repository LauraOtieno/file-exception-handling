# --- Assignment 1: Smartphone Class with Inheritance ---
class Smartphone:
    def __init__(self, brand, model): self.brand, self.model = brand, model
    def make_call(self, num): print(f"{self.brand} {self.model} calling {num}...")

class Android(Smartphone):
    def move(self): print(f"{self.brand} {self.model} runs Android 📱")

class iPhone(Smartphone):
    def move(self): print(f"{self.brand} {self.model} runs iOS 🍎")

# --- Assignment  2: Polymorphism with Vehicles ---
class Vehicle:  def move(self): pass
class Car(Vehicle):   def move(self): print("Driving 🚗")
class Plane(Vehicle): def move(self): print("Flying ✈️")

phone1, phone2 = Android("Samsung", "S23"), iPhone("Apple", "15")
phone1.make_call("0712345678"); phone1.move()
phone2.make_call("0798765432"); phone2.move()

for v in [Car(), Plane()]: v.move()
