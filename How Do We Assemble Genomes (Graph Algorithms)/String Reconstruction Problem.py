def start_node(adj_list):
    in_degrees = {node: 0 for node in adj_list}
    for node, neighbors in adj_list.items():
        in_degrees[node] -= len(neighbors)
        for neighbor in neighbors:
            if neighbor in in_degrees:
                in_degrees[neighbor] += 1
            else:
                in_degrees[neighbor] = 1
    for node, in_degree in in_degrees.items():
        if in_degree == -1:
            first_node = node
            return first_node
def string_reconstruction(k, kmers):
    adj_list = {}
    for kmer in kmers:
        prefix = kmer[:k - 1]
        suffix = kmer[1:]
        if prefix in adj_list:
            adj_list[prefix].append(suffix)
        else:
            adj_list[prefix] = [suffix]
    first_node = start_node(adj_list)
    path = [first_node]
    while adj_list:
        if path[-1] in adj_list:
            current_node = path[-1]
            next_node = adj_list[current_node].pop()
            if len(adj_list[current_node]) == 0:
                del adj_list[current_node]
            path.append(next_node)
        else:
            for i in range(len(path)):
                if path[i] in adj_list:
                    cycle = path[i:]
                    del path[i:]
                    path += cycle
                    break
    return ''.join([node[0] for node in path]) + path[-1][1:]

k = int(input())
input_kmers = []
while True:
    try:
        pattern = input()
        if pattern == '':
            break
        input_kmers.append(pattern)
    except:
        break

result = string_reconstruction(k, input_kmers)
print(result)
