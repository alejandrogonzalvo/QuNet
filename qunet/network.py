from qunet.core import Core
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

class Network:
    id: int = 0
    cores: list[Core] = []
    edges: list[tuple[int, int]] = []

    def __init__(self, id: int, cores: list[Core]=[], edges: list[tuple[int, int]]=[]):
        self.id = id
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

    def plot(self):
        G = nx.Graph()
        for core in self.cores:
            G.add_node(core.id)
        G.add_edges_from(self.edges)
        nx.draw(G, with_labels=True)
        plt.show()

    @staticmethod
    def grid2D(id: int, core: Core, x: int, y: int):
        total: int = x*y
        
        n : Network = Network(id)
        for i in range(total):
            core.id = i
            n.cores.append(deepcopy(core))

            if i % x != 0:
                n.edges.append((i-1, i))
            if i >= x:
                n.edges.append((i-x, i))
        
        return n

    