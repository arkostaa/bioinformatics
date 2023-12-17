def de_bruijn_graph(kmers):
    adj_list = {}

    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix in adj_list:
            adj_list[prefix].append(suffix)
        else:
            adj_list[prefix] = [suffix]

    return adj_list

kmers = []

while True:
    try:
        pattern = input()
        if pattern == '':
            break
        kmers.append(pattern)
    except:
        break

result = de_bruijn_graph(kmers)

for key in sorted(result.keys()):
    print(key, '->', ','.join(sorted(result[key])))