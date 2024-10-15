"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,

Key Points:
- Purpose: Allows subclasses to choose the class of object to instantiate.
- Use case: When the creation process involves some logic, and subclasses may differ slightly.
"""


class Car:
    def drive(self):
        return "Car is being driven"


class Truck:
    def drive(self):
        return "Truck is being driven"


class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()


factory = VehicleFactory()
vehicle = factory.create_vehicle("car")
print(vehicle.drive())
