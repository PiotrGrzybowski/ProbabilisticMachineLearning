import itertools
import networkx as nx
import matplotlib.pyplot as plt
import tqdm
from PIL import Image
from networkx.drawing.nx_agraph import to_agraph
from networkx.algorithms.traversal.depth_first_search import dfs_edges

from Lab10.graph_utils import generate_random_dag, are_nodes_d_separated_by_observation, get_random_color

graph = nx.DiGraph()

graph.add_nodes_from(range(1, 11))
graph.add_edges_from([(1, 3),
                      (2, 3),
                      (3, 4),
                      (3, 8),
                      (4, 6),
                      (5, 6),
                      (6, 7),
                      (7, 9),
                      (10, 9)])

# for x in nx.all_simple_paths(graph.to_undirected(), 1, 2):
#     print(x)
# for edge in dfs_edges(graph, 6):
#     print(type(edge))


# graph = generate_random_dag(10, 0.3)
#
# A = to_agraph(graph)
# A.node_attr['style'] = 'filled'
# n = A.get_node('1')
# n.attr['fillcolor']="#CCCCFF"
# n.attr['label'] = '1'
# A.layout()
# A.layout(prog='dot')
# A.draw('file.png')
# img = Image.open('file.png')
# plt.imshow(img)
# plt.show()


#######OWN#################
graph = nx.DiGraph()
nodes = [1, 2, 3, 4, 5, 6, 7, 8]
graph.add_nodes_from(nodes)
edges = [(1, 3), (2, 3), (3, 4), (3, 8), (4, 6), (5, 6), (6, 7)]
graph.add_edges_from(edges)


######RANDOM##########
# graph = generate_random_dag(10, 0.2)


#OBSERVATION
observation = {3}
pairs = list(itertools.combinations(nodes, 2))
result = {}

for pair in pairs:
    d_separated = are_nodes_d_separated_by_observation(graph, *pair, observation)
    print("{}, {}: {}".format(pair[0], pair[1], d_separated))
    print()
    result[pair] = d_separated

A = to_agraph(graph)
A.node_attr['style'] = 'filled'

# for pair, d_separated in result.items():
#     if d_separated:
#         color = get_random_color()
#         n = A.get_node(pair[0])
#         n.attr['fillcolor'] = "#CCCCFF"
#
#         n = A.get_node(pair[1])
#         n.attr['fillcolor'] = "#CCCCFF"

for o in observation:
    n = A.get_node(o)
    n.attr['fillcolor'] = 'red'

A.layout()
A.layout(prog='dot')
A.draw('file.png')
img = Image.open('file.png')
plt.imshow(img)
plt.show()