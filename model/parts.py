class Parts:
    def __init__(self, id: int, name: str, total_in_stock: int) -> None:
        self.id = id
        self.name = name
        self.total_in_stock = total_in_stock
class Used_Part:
    def __init__(self, part: Parts, required: int) -> None:
        self.part = part
        self.required = required