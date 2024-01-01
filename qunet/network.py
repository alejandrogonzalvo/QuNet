from qunet.core import Core
import qunet.id_manager as id_manager

import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

class Network:
    id: int = 0
    cores: list[Core] = []
    edges: list[tuple[int, int]] = []

    def __init__(self, cores: list[Core]=[], edges: list[tuple[int, int]]=[]):
        self.id = id_manager._network_id
        id_manager._network_id += 1
        self.cores = cores
        self.edges = edges
    
    def __json__(self) -> dict:
        return {
            'network': {
                'id': self.id,
                'cores': self.cores,
                'edges': self.edges
            }
        }
    
    def add_core(self, c: Core) -> None:
        if c in self.cores:
            raise Exception(f"core with ID={c.id} already exists in Network with ID={self.id}")

        self.cores.append(c)

    def plot(self):
        G = nx.Graph()
        for core in self.cores:
            G.add_node(core.id)
        G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True)
        plt.show()

    @staticmethod
    def grid2D(core: Core, x: int, y: int):
        total: int = x*y
        
        n : Network = Network()
        n.add_core(core)
        for i in range(1, total):
            n.add_core(Core(deepcopy(core.qubits), deepcopy(core.edges), deepcopy(core.gates)))

            if i % x != 0:
                n.edges.append((i-1, i))
            if i >= x:
                n.edges.append((i-x, i))
        
        return n

    