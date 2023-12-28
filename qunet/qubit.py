class Qubit:
    id: int = 0

    def __init__(self, id):
        self.id = id

    def __json__(self) -> dict:
        return {
            'qubit': {
                'id': self.id
            }
        }