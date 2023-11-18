def prob_kmer(s, Matrix):
    P = 1
    for i in range(len(s)):
        nucleotide = s[i]
        if nucleotide == 'A':
            P *= Matrix[0][i]
        elif nucleotide == 'C':
            P *= Matrix[1][i]
        elif nucleotide == 'G':
            P *= Matrix[2][i]
        elif nucleotide == 'T':
            P *= Matrix[3][i]
    return P

def most_prob_kmer(DNA, k, Matrix):
    seq = {}
    for i in range(len(DNA) - k + 1):
        seq[DNA[i:i + k]] = prob_kmer(DNA[i:i + k], Matrix)
    for i in seq.keys():
        if seq[i] == max(seq.values()):
            return i

def Profile(M):
    k = len(M[0])
    Profile = [[0] * k for _ in range(4)]
    for st in M:
        for i in range(len(st)):
            nucleotide = st[i]
            if nucleotide == "A":
                Profile[0][i] += (1 / len(M))
            elif nucleotide == "C":
                Profile[1][i] += (1 / len(M))
            elif nucleotide == "G":
                Profile[2][i] += (1 / len(M))
            elif nucleotide == "T":
                Profile[3][i] += (1 / len(M))
    return Profile

def greedy_motif_search(DNA, k, t):
    res = []
    for st in DNA:
        res.append(st[0:k])
    for i in range(len(DNA[0]) - k + 1):
        M = []
        M.append(DNA[0][i:i + k])
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
DNA = []
for _ in range(t):
    DNA.append(input())
res = greedy_motif_search(DNA, k, t)
for i in res:
    print(i)