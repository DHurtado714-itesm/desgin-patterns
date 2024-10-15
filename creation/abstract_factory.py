"""
The Abstract Factory pattern creates families of related objects without specifying their concrete classes.

Key Points:
- Purpose: Create families of related objects.
- Use case: When dealing with multiple families of products or components, like GUI toolkits where widgets vary between operating systems.
"""


class Car:
    def create(self):
        return "Car created"


class Truck:
    def create(self):
        return "Truck created"


class VehicleFactory:
    def create_car(self):
        return Car()

    def create_truck(self):
        return Truck()


factory = VehicleFactory()
car = factory.create_car()
truck = factory.create_truck()

print(car.create())
print(truck.create())
