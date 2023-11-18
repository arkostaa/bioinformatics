def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

def generate_neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']

    neighbors = []
    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighbors.append(nucleotide + text)
        else:
            neighbors.append(pattern[0] + text)

    return neighbors

def motif_enumeration(DNA, k, d):
    patterns = set()
    for sequence in DNA:
        for i in range(len(sequence) - k + 1):
            pattern = sequence[i:i+k]
            neighbors = generate_neighbors(pattern, d)
            for neighbor in neighbors:
                count = 0
                for seq in DNA:
                    if is_pattern_present(seq, neighbor, k, d):
                        count += 1
                if count == len(DNA):
                    patterns.add(neighbor)
    return patterns

def is_pattern_present(seq, pattern, k, d):
    for j in range(len(seq) - k + 1):
        subsequence = seq[j:j+k]
        if hamming_distance(subsequence, pattern) <= d:
            return True
    return False

k, d = map(int, input().split(" "))
DNA = []
str_input = " "
while str_input != "":
    try:
        str_input = input()
        DNA.append(str_input)
    except:
        break

result = list(motif_enumeration(DNA, k, d))
result.sort()
print(*result)