from itertools import islice
import networkx as nx

TAIL_TO_TAIL = 1
HEAD_TO_HEAD = -1
HEAD_TO_TAIL = 0


def is_path_blocked_by_observation(graph, path, observation):
    for segment in get_segments_from_path(path):
        pass


def get_segment_type(graph, segment):
    if nx.has_path(graph, segment[1], segment[0]) and nx.has_path(graph, segment[1], segment[2]):
        return TAIL_TO_TAIL
    elif nx.has_path(graph, segment[0], segment[1]) and nx.has_path(graph, segment[2], segment[1]):
        return HEAD_TO_HEAD
    else:
        return HEAD_TO_TAIL


def get_segments_from_path(path):
    it = iter(path)
    result = tuple(islice(it, 3))
    if len(result) == 3:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def get_descendants(graph, source):
    return nx.descendants(graph, source)


def generate_random_dag(n, p):
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    return nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
