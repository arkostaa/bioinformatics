import random

def most_probable_kmer(text, k, profile):
    max_prob = -1
    most_prob_kmer = ""
    n = len(text)
    for i in range(n - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            nucleotide = kmer[j]
            prob *= profile[nucleotide][j]
        if prob > max_prob:
            max_prob = prob
            most_prob_kmer = kmer
    return most_prob_kmer

def create_profile_matrix(motifs, k, pseudocounts=True):
    profile = {
        'A': [0] * k,
        'C': [0] * k,
        'G': [0] * k,
        'T': [0] * k
    }
    t = len(motifs)

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(t):
            nucleotide = motifs[j][i]
            count[nucleotide] += 1
        if pseudocounts:
            for nucleotide in count:
                count[nucleotide] += 1
        for nucleotide in count:
            profile[nucleotide][i] = count[nucleotide] / (t + 4) if pseudocounts else count[nucleotide] / t
    return profile

def score_motifs(motifs):
    consensus = ""
    t = len(motifs)
    k = len(motifs[0])
    score = 0

    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(t):
            nucleotide = motifs[j][i]
            count[nucleotide] += 1

        max_count = max(count.values())
        consensus += [key for key, value in count.items() if value == max_count][0]
        score += t - max_count
    return score


def randomized_motif_search(DNA, k, t):
    best_motifs = [DNA[i][random.randint(0, len(DNA[i]) - k):][:k] for i in range(t)]

    while True:
        profile = create_profile_matrix(best_motifs, k)
        motifs = [most_probable_kmer(seq, k, profile) for seq in DNA]
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


def randomized_motif_search_multiple_times(DNA, k, t, num_iterations):
    best_motifs = None
    best_score = float('inf')

    for _ in range(num_iterations):
        motifs = randomized_motif_search(DNA, k, t)
        score = score_motifs(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs

k, t = map(int, input().split())
DNA = [input() for _ in range(t)]

best_motifs = randomized_motif_search_multiple_times(DNA, k, t, 1000)
for motif in best_motifs:
    print(motif)
