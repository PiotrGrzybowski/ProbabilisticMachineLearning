from itertools import islice
import networkx as nx
import random

TAIL_TO_TAIL = 1
HEAD_TO_HEAD = -1
HEAD_TO_TAIL = 0


def is_path_blocked_by_observation(graph, path, observation):
    segments = list(get_segments_from_path(path))
    if len(segments) == 0:
        return False

    for segment in get_segments_from_path(path):
        segment_type = get_segment_type(graph, segment)

        if segment_type == HEAD_TO_HEAD:
            if segment[1] not in observation and len(get_descendants(graph, segment[1]) & observation) == 0:
                return True
        elif segment_type == HEAD_TO_TAIL or segment_type == TAIL_TO_TAIL:
            if segment[1] in observation:
                return True

    return False


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


def are_nodes_d_separated_by_observation(graph, source, target, observation):
    paths = list(nx.all_simple_paths(graph.to_undirected(), source, target))
    print("Paths = {}".format(len(paths)))
    for path in paths:
        print(path)
        if not is_path_blocked_by_observation(graph, path, observation):
            return False

    return True


def get_random_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())