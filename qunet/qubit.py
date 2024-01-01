import qunet.id_manager as id_manager

class Qubit:
    id: int = 0

    def __init__(self):
        self.id = id_manager._qubit_id
        id_manager._qubit_id += 1

    def __json__(self) -> dict:
        return {
            'qubit': {
                'id': self.id
            }
        }