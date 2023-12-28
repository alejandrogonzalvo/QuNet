from qunet.qubit import Qubit
from qunet.gate import Gate
import networkx as nx
import matplotlib.pyplot as plt
import json

class Core:
    id: int = 0
    qubits: list[Qubit] = []
    edges: list[tuple[int, int]] = []
    gates: list[Gate] = []

    def __init__(self, id: int, qubits: list[Qubit]=[], edges: list[tuple[int, int]]=[], gates: list[Gate]=[]):
        self.id = id
        self.qubits = qubits
        self.edges = edges
        self.gates = gates
    
    def __json__(self) -> dict:
        return {
            'core': {
                'id': self.id,
                'qubits': self.qubits,
                'edges': self.edges,
                'gates': self.gates
            }
        }
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__json__(), indent=4)
    
    def plot(self):
        G = nx.Graph()
        for qubit in self.qubits:
            G.add_node(qubit.id)
        G.add_edges_from(Core.edges)
        nx.draw(G, with_labels=True)
        plt.show()
    
    def get_gate_ids(self):
        return [gate.id for gate in self.gates]
    
    def get_qubit_ids(self):
        return [qubit.id for qubit in self.qubits]