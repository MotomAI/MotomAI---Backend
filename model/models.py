from xmlrpc.client import Boolean
from model.parts import Parts


class Model:
    def __init__(self, id: int, name: str, year:int, brand: str, parts, warn: bool, graph: str = None) -> None:

        self.id = id
        self.name = name
        self.year = year
        self.brand = brand
        self.parts = parts
        self.warn = warn
