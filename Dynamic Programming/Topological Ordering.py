from collections import defaultdict
from collections import deque

def build_graph(edges):
    graph = defaultdict(list)
    points = []
    for edge in edges:
        start, end = edge.split(' -> ')
        for point in end.split(','):
            points.append(point)
        for point in points:
            graph[int(start)].append(int(point))
        points = []
    return graph

def topological_sort(edges):
    adj_list = build_graph(edges)
    edges_count = defaultdict(int)
    for node in adj_list:
        for neighbor in adj_list[node]:
            edges_count[neighbor] += 1

    queue = deque(node for node in adj_list if edges_count[node] == 0)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj_list[node]:
            edges_count[neighbor] -= 1
            if edges_count[neighbor] == 0:
                queue.append(neighbor)

    return result

edges_list = []

while True:
    try:
        edge_input = input()
        if edge_input == '':
            break
        edges_list.append(edge_input)
    except:
        break

topological_order = topological_sort(edges_list)
print(", ".join(map(str, topological_order)))