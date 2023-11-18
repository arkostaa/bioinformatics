def prob_kmer(s, matrix):
    P = 1
    for i, nucleotide in enumerate(s):
        if nucleotide == 'A':
            P *= matrix[0][i]
        elif nucleotide == 'C':
            P *= matrix[1][i]
        elif nucleotide == 'G':
            P *= matrix[2][i]
        elif nucleotide == 'T':
            P *= matrix[3][i]
    return P

def most_prob_kmer(DNA, k, matrix):
    seq = {DNA[i:i + k]: prob_kmer(DNA[i:i + k], matrix) for i in range(0, len(DNA) - k + 1)}
    return max(seq, key=seq.get)

def Profile(M):
    k = len(M[0])
    Prof = [[1 / len(M)] * k for _ in range(4)]
    for st in M:
        for i, nucleotide in enumerate(st):
            if nucleotide == "A":
                Prof[0][i] += (1 / len(M))
            elif nucleotide == "C":
                Prof[1][i] += (1 / len(M))
            elif nucleotide == "G":
                Prof[2][i] += (1 / len(M))
            elif nucleotide == "T":
                Prof[3][i] += (1 / len(M))
    return Prof

def greedy_motif_search(DNA, k, t):
    res = [st[0:k] for st in DNA]
    for i in range(len(DNA[0]) - k + 1):
        M = [DNA[0][i:i + k]]
        for j in range(1, t):
            M.append(most_prob_kmer(DNA[j], k, Profile(M)))
        if Score(res) > Score(M):
            res = M
    return res

def Score(motifs):
    res = 0
    st = ""
    profile = Profile(motifs)
    for i in range(len(profile[0])):
        max_p = 0
        sym = 0
        for sym in range(4):
            if profile[sym][i] > max_p:
                s = sym
                max_p = profile[sym][i]
        if s == 0:
            st += "A"
        elif s == 1:
            st += "C"
        elif s == 2:
            st += "G"
        elif s == 3:
            st += "T"
    for string in motifs:
        for i in range(len(string)):
            if st[i] != string[i]:
                res += 1
    return res

k, t = map(int, input().split())
DNA = [str(input()) for _ in range(t)]
res = greedy_motif_search(DNA, k, t)
for i in res:
    print(i)
