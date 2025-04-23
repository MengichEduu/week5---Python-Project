# Base class for animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Dog
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Subclass for Fish
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Function to demonstrate polymorphism
def demonstrate_movement(moving_objects):
    for obj in moving_objects:
        obj.move()

# Creating instances of animals and vehicles
dog = Dog()
fish = Fish()
car = Car()
plane = Plane()

# List of all objects
moving_objects = [dog, fish, car, plane]

# Demonstrating movement for all objects
demonstrate_movement(moving_objects)