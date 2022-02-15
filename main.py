from networkx import DiGraph, edge_bfs
from os.path import isfile
from operator import add


def read_input(file_name: str, graph: DiGraph, set1: list, set2: list) -> None:
    with open(file_name, 'r') as file:
        n, m = map(int, file.readline().split())
        graph.add_nodes_from(range(1, n + 1))
        for _ in range(m):
            u, v = map(int, file.readline().split())
            graph.add_edge(u, v)
        file.readline()  # number of nodes in set1, useless
        set1 += list(map(int, file.readline().split()))
        file.readline()  # number of nodes in set2, useless
        set2 += list(map(int, file.readline().split()))


def find_dists(graph: DiGraph, node_set: list, dists: list) -> None:
    for v in node_set:
        dists[v] = 0
    for u, v, _ in edge_bfs(graph, node_set, 'reverse'):
        dists[u] = min(dists[u], dists[v] + 1)


def solve(graph: DiGraph, set1: list, set2: list) -> list:
    n = graph.number_of_nodes()
    dists1 = [2 * n + 1 for v in range(n + 1)]
    find_dists(graph, set1, dists1)
    dists2 = [2 * n + 1 for v in range(n + 1)]
    find_dists(graph, set2, dists2)
    dists = list((zip(range(n + 1), map(add, dists1, dists2))))
    dists = list(filter(lambda x: x[1] <= 2 * n, dists[1:]))
    dists.sort()
    return [v for v, _ in dists]


def print_answer(file_name: str, answer: list) -> None:
    with open(file_name, 'w') as file:
        for v in answer:
            file.write(str(v) + '\n')


def main(in_name: str, out_name: str) -> None:
    if not isfile(in_name):
        raise FileNotFoundError('Input file does not exist')
    graph = DiGraph()
    set1 = []
    set2 = []
    try:
        read_input(in_name, graph, set1, set2)
    except ValueError:
        raise ValueError('Incorrect input file format')
    answer = solve(graph, set1, set2)
    print_answer(out_name, answer)


if __name__ == '__main__':
    input_file_name = 'test_files/dummy_tests/test1/input.txt'
    output_file_name = 'test_files/dummy_tests/test1/output.txt'
    main(input_file_name, output_file_name)
