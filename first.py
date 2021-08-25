import itertools
import random
import math
import networkx as nx
from networkx.generators.classic import empty_graph, path_graph, complete_graph
from networkx.generators.random_graphs import erdos_renyi_graph
n = 6
p = 0.5
g = erdos_renyi_graph(n, p)

print(g.nodes)
print(g.edges)
