class Qubit:
    id: int = 0

    def __init__(self, id):
        self.id = id

    def __str__(self) -> str:
        return self.id