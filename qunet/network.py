from qunet.core import Core
import qunet.id_manager as id_manager

import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

class Network:
    id: int = 0
    cores: list[Core] = []
    edges: list[tuple[Core, Core]] = []

    def __init__(self, cores: list[Core]=[], edges: list[tuple[Core, Core]]=[]):
        self.id = id_manager._network_id
        id_manager._network_id += 1
        self.cores = cores
        self.edges = edges
    
    def __json__(self) -> dict:
        return {
            'network': {
                'id': self.id,
                'cores': self.cores,
                'edges': self._get_edges()
            }
        }
    
    def _get_edges(self) -> list[tuple[int, int]]:
        return [(edge[0].id, edge[1].id) for edge in self.edges]
    
    def add_core(self, c: Core) -> int:
        if c in self.cores:
            raise Exception(f"core with ID={c.id} already exists in Network with ID={self.id}")

        self.cores.append(c)
        return c.id
    
    def get_core(self, id: int) -> Core:
        for core in self.cores:
            if core.id == id:
                return core
        raise Exception(f"core with ID={id} does not exist in Network with ID={self.id}")

    def plot(self):
        G = nx.Graph()
        for core in self.cores:
            G.add_node(core.id)
        G.add_edges_from(self._get_edges())
        nx.draw(G, with_labels=True)
        plt.show()

    @staticmethod
    def grid2D(core: Core, x: int, y: int):
        total: int = x*y
        
        n : Network = Network()
        n.add_core(core)
        for i in range(1, total):
            id: int = n.add_core(Core.copy(core))

            if i % x != 0:
                n.edges.append((n.get_core(id), n.get_core(id-1)))
            if i >= x:
                n.edges.append((n.get_core(id-x), n.get_core(id)))
        
        return n
    