import copy

"""
Prototype pattern creates new objects by copying an existing one.

Key Points:
- Purpose: Clone existing instances.
- Use case: Costly object initialization.
"""


class Prototype:
    def __init__(self, value) -> None:
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


prototype = Prototype([1, 2, 3])
clone = prototype.clone()
print(clone.value)
