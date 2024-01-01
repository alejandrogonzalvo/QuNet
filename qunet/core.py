from qunet.qubit import Qubit
from qunet.gate import Gate
import networkx as nx
import matplotlib.pyplot as plt
import json
import qunet.id_manager as id_manager
from copy import deepcopy

class Core:
    id: int = 0
    qubits: list[Qubit] = []
    edges: list[tuple[Qubit, Qubit]] = []
    gates: list[Gate] = []

    def __init__(self, qubits: list[Qubit]=[], edges: list[tuple[Qubit, Qubit]]=[], gates: list[Gate]=[]):
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
    
    def _get_edges(self) -> list[tuple[int, int]]:
        return [(edge[0].id, edge[1].id) for edge in self.edges]
    
    def add_qubit(self, q: Qubit) -> int:
        if q in self.qubits:
            raise Exception(f"qubit with ID={q.id} already exists in Core with ID={self.id}")

        self.qubits.append(q)
        return q.id
    
    def get_qubit(self, id: int) -> Qubit:
        for qubit in self.qubits:
            if qubit.id == id:
                return qubit
        raise Exception(f"Qubit with ID={id} not found in Core with ID={self.id}")

    def plot(self):
        G = nx.Graph()
        for qubit in self.qubits:
            G.add_node(qubit.id)
        G.add_edges_from(self._get_edges())
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
            id = c.add_qubit(Qubit())

            if i % x != 0:
                c.edges.append((c.get_qubit(id-1), c.get_qubit(id)))
            if i >= x:
                c.edges.append((c.get_qubit(id-x), c.get_qubit(id)))
        
        return c
    
    @staticmethod
    def copy(core):
        c: Core = deepcopy(core)
        c.id = id_manager._core_id
        id_manager._core_id += 1

        for qubit in c.qubits:
            qubit.id = id_manager._qubit_id
            id_manager._qubit_id += 1
        
        for gate in c.gates:
            gate.id = id_manager._gate_id
            id_manager._gate_id += 1

        return c