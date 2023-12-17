import sys
from collections import defaultdict


def eulerian_cycle(graph):
    def visit(node):
        while graph[node]:
            visit(graph[node].pop())
        circuit.append(node)

    circuit = []

    graph_copy = defaultdict(list)
    for node, neighbors in graph.items():
        graph_copy[node] = neighbors[:]

    start_node = list(graph_copy.keys())[0]

    visit(start_node)

    circuit.reverse()

    return "->".join(map(str, circuit))


graph = defaultdict(list)
for line in sys.stdin:
    line = line.strip()
    if not line:
        break

    parts = line.split("->")
    if len(parts) == 2:
        try:
            from_node = int(parts[0].strip())
            to_nodes = list(map(int, parts[1].split(',')))
            graph[from_node] = to_nodes
        except:
            break

result = eulerian_cycle(graph)
print(result)