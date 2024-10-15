"""
Adapter pattern allows incompatible interfaces to work together by wrapping an existing class with a new interface.

Key Points:
- Purpose: Make incompatible interfaces compatible.
- Use case: When you have to work with an existing class but the interface is not what the client code expects.
"""


class EuropeanSocket:
    def voltage(self):
        return 230


class USAdapter:
    def __init__(self, eu_socket) -> None:
        self.eu_socket = eu_socket

    def votage(self):
        return 110


eu_socket = EuropeanSocket()
adapter = USAdapter(eu_socket)

print(adapter.votage())
