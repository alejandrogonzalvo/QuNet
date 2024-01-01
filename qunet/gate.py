import qunet.id_manager as id_manager

class Gate:
    id: int = 0
    error_rate: float = 0.0
    gate_time: float = 0.0

    def __init__(self, error_rate, gate_time):
        self.id = id_manager._gate_id
        id_manager._gate_id += 1
        
        self.error_rate = error_rate
        self.gate_time = gate_time

    def __json__(self) -> dict:
        return {
            'gate': {
                'id': self.id,
                'error_rate': self.error_rate,
                'gate_time': self.gate_time
            }
        }