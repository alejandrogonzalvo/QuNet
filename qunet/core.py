from qunet.qubit import Qubit
from qunet.gate import Gate
import networkx as nx
import matplotlib.pyplot as plt
import json
import qunet.id_manager as id_manager

class Core:
    id: int = 0
    qubits: list[Qubit] = []
    edges: list[tuple[int, int]] = []
    gates: list[Gate] = []

    def __init__(self, qubits: list[Qubit]=[], edges: list[tuple[int, int]]=[], gates: list[Gate]=[]):
        self.id = id_manager._core_id
        id_manager._core_id += 1
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
    
    def add_qubit(self, q: Qubit) -> None:
        if q in self.qubits:
            raise Exception(f"qubit with ID={q.id} already exists in Core with ID={self.id}")

        self.qubits.append(q)

    def plot(self):
        G = nx.Graph()
        for qubit in self.qubits:
            G.add_node(qubit.id)
        G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True)
        plt.show()
    
    def get_gate_ids(self):
        return [gate.id for gate in self.gates]
    
    def get_qubit_ids(self):
        return [qubit.id for qubit in self.qubits]
    
    @staticmethod
    def grid2D(x: int, y: int):
        total: int = x*y
        
        c : Core = Core()
        for i in range(total):
            c.add_qubit(Qubit())

            if i % x != 0:
                c.edges.append((i-1, i))
            if i >= x:
                c.edges.append((i-x, i))
        
        return c