"""
Builder pattern constructs a complex object step by step.

Key Points:
- Purpose: Step-by-step construction of a complex object.
- Use case: Creating objects with many optional parameters or components.
"""


class House:
    def __init__(self):
        self.window = 0
        self.doors = 0
        self.garage = False

    def __str__(self) -> str:
        return f"House with {self.window} windows, {self.doors} doors and garage: {self.garage}"


class HouseBuilder:
    def __init__(self) -> None:
        self.house = House()

    def build_window(self, count: int):
        self.house.window = count
        return self

    def build_doors(self, count: int):
        self.house.doors = count
        return self

    def build_garage(self):
        self.house.garage = True
        return self

    def build(self):
        return self.house


builder = HouseBuilder()
house = builder.build_window(4).build_doors(2).build_garage().build()
print(house)
