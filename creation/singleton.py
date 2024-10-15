"""
Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

Key Points:
- Purpose: Ensure a single instance of the class.
- Use case: Logger class, database connections, configuration classes, etc.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
