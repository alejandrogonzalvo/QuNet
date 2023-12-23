from qunet.qubit import Qubit
from qunet.gate import Gate
import networkx as nx
import matplotlib.pyplot as plt

class Core:
    id: int = 0
    qubits: list[Qubit] = []
    edges: list[tuple[int, int]] = []
    gates: list[Gate] = []

    def plot(self):
        G = nx.Graph()
        for qubit in self.qubits:
            G.add_node(qubit.id)
        G.add_edges_from(Core.edges)
        nx.draw(G, with_labels=True)
        plt.show()

    def get_qubit_ids(self) -> list[int]:
        return [qubit.id for qubit in self.qubits]

    def get_gate_ids(self) -> list[int]:
        return [gate.id for gate in self.gates]


# core1: Core = Core()

# for i in range(R):
#     core1.qubits.append(Qubit(i))

# for qubit in core1.qubits:
#     if qubit.id % M != M-1:
#         core1.edges.append((qubit.id, qubit.id+1))
#     if qubit.id % M != 0:
#         core1.edges.append((qubit.id, qubit.id-1))
    
#     if qubit.id < R-M:
#         core1.edges.append((qubit.id, qubit.id+M))
    
#     if qubit.id >= M:
#         core1.edges.append((qubit.id, qubit.id-M))

# core1.plot()