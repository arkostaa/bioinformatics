from collections import defaultdict
def longest_path_in_dag(source, sink, edges):
    graph = defaultdict(list)
    for edge in edges:
        start, end_weight = edge.split('->')
        end, weight = end_weight.split(':')
        graph[int(start)].append((int(end), int(weight)))

    def topological_sort():
        visited = set()
        topo_order = []

        def dfs(node, topo_order):
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, topo_order)
            topo_order.append(node)

        keys = list(graph.keys())
        for node in keys:
            if node not in visited:
                dfs(node, topo_order)

        return list(reversed(topo_order))

    topo_order = topological_sort()

    arr = {node: float('-inf') for node in graph}
    arr[source] = 0
    parent = {node: None for node in graph}

    for node in topo_order:
        for neighbor, weight in graph[node]:
            if arr[neighbor] < arr[node] + weight:
                arr[neighbor] = arr[node] + weight
                parent[neighbor] = node

    longest_path = []
    node = sink
    while node is not None:
        longest_path.append(str(node))
        node = parent[node]
    longest_path = '->'.join(reversed(longest_path))

    return arr[sink], longest_path

source_node = int(input())
sink_node = int(input())
edges_list = []

while True:
    try:
        edge_input = input()
        if edge_input == '':
            break
        edges_list.append(edge_input)
    except:
        break

result_length, result_path = longest_path_in_dag(source_node, sink_node, edges_list)
print(result_length)
print(result_path)
