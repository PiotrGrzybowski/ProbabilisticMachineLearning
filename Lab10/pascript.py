import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
from networkx.drawing.nx_agraph import to_agraph
from networkx.algorithms.traversal.depth_first_search import dfs_edges

from Lab10.graph_utils import generate_random_dag

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

# nx.draw(graph, with_labels=True, node_size=300)
# plt.show()
# for x in nx.all_simple_paths(graph.to_undirected(), 1, 2):
#     print(x)
# for edge in dfs_edges(graph, 6):
#     print(type(edge))
#
#
# print(nx.descendants(graph, 6))

graph = generate_random_dag(10, 0.3)

A = to_agraph(graph)
A.node_attr['style'] = 'filled'
n = A.get_node('1')
n.attr['fillcolor']="#CCCCFF"
n.attr['label'] = '1'
A.layout()
A.layout(prog='dot')
A.draw('file.png')
img = Image.open('file.png')
plt.imshow(img)
plt.show()

# print(nx.has_path(graph, 9, 7))