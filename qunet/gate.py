class Gate:
    id: int = 0
    error_rate: float = 0.0
    gate_time: float = 0.0

    def __init__(self, error_rate, gate_time):
        self.error_rate = error_rate
        self.gate_time = gate_time

    def __str__(self) -> str:
        return self.id