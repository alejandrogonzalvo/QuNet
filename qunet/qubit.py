class Qubit:
    id: int = 0

    def __init__(self):
        self.id = Qubit.id
        Qubit.id += 1

    def __json__(self) -> dict:
        return {
            'qubit': {
                'id': self.id
            }
        }