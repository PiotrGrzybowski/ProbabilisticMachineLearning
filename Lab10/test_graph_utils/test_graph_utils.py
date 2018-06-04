import networkx as nx
import unittest

from Lab10.graph_utils import TAIL_TO_TAIL, get_segment_type, HEAD_TO_HEAD, HEAD_TO_TAIL, get_segments_from_path, \
    generate_random_dag, get_descendants


class TestGraphUtils(unittest.TestCase):
    def test_get_segment_type_head_to_head(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([1, 2, 3])
        graph.add_edges_from([(1, 2), (3, 2)])

        self.assertEqual(get_segment_type(graph, [1, 2, 3]), HEAD_TO_HEAD)

    def test_get_segment_type_tail_to_tail(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([1, 2, 3])
        graph.add_edges_from([(2, 1), (2, 3)])

        self.assertEqual(get_segment_type(graph, [1, 2, 3]), TAIL_TO_TAIL)

    def test_get_segment_type_head_to_tal_left(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([1, 2, 3])
        graph.add_edges_from([(1, 2), (2, 3)])

        self.assertEqual(get_segment_type(graph, [1, 2, 3]), HEAD_TO_TAIL)

    def test_get_segment_type_head_to_tal_right(self):
        graph = nx.DiGraph()
        graph.add_nodes_from([1, 2, 3])
        graph.add_edges_from([(3, 2), (2, 1)])

        self.assertEqual(get_segment_type(graph, [1, 2, 3]), HEAD_TO_TAIL)

    def test_get_segments_from_path(self):
        path = [1, 2, 3, 4, 5]

        self.assertEqual(list(get_segments_from_path(path)), [(1, 2, 3), (2, 3, 4), (3, 4, 5)])

    def test_get_descendants(self):
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

        self.assertEqual(get_descendants(graph, 6), {7, 9})

    def test_generate_random_dag(self):
        self.assertTrue(nx.is_directed_acyclic_graph(generate_random_dag(10, 0.5)))


if __name__ == '__main__':
    unittest.main()
