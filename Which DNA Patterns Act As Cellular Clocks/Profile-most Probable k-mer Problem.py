def ProbKmer(s, Matrix):
    P = 1
    for i in range(len(s)):
        if s[i] == 'A':
            P *= Matrix[0][i]
        elif s[i] == 'C':
            P *= Matrix[1][i]
        elif s[i] == 'G':
            P *= Matrix[2][i]
        elif s[i] == 'T':
            P *= Matrix[3][i]
    return P

DNA = input()
k = int(input())

Matrix = [[0] * k for _ in range(4)]
for i in range(4):
    Matrix[i] = list(map(float, input().split()))

seq = {}
for i in range(len(DNA) - k + 1):
    seq[DNA[i:i + k]] = ProbKmer(DNA[i:i + k], Matrix)

max_prob = max(seq.values())
for i in seq.keys():
    if seq[i] == max_prob:
        print(i)