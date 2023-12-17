from collections import defaultdict

def eulerian_path(graph):
    def dfs(curr_node):
        while curr_node in graph and graph[curr_node]:
            next_curr_node = graph[curr_node].pop(0)
            dfs(next_curr_node)
            path.append(next_curr_node)

    path = []
    start_node = None

    for curr_node in graph:
        out_degree = len(graph[curr_node])
        in_degree = sum(1 for vertices in graph.values() if curr_node in vertices)
        if in_degree < out_degree:
            start_node = curr_node

    if start_node:
        dfs(start_node)
    else:
        start_node = next(iter(graph))
        dfs(start_node)

    return [start_node] + path[::-1]

adjacency_list = defaultdict(list)
while True:
    try:
        line = input().strip()
        if not line:
            break
        parts = line.split(" -> ")
        if len(parts) == 2:
            from_node = int(parts[0].strip())
            to_nodes = list(map(int, parts[1].split(',')))
            adjacency_list[from_node] = to_nodes
    except:
        break

result = eulerian_path(adjacency_list)
print("->".join(map(str, result)))
