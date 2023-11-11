# CODE CHALLENGE: Implement LeaderboardCyclopeptideSequencing.
#      Input: An integer N and a collection of integers Spectrum.
#      Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).
# Note: Multiple solutions may exist. You may return any one.
#
# Sample Input:
#
# 10
# 0 71 113 129 147 200 218 260 313 331 347 389 460
# Sample Output:
#
# 71-147-113-129

def linear_score(peptide, spectrum_dict):
    if len(peptide) == 0:
        return 0
    aa_list = [int(aa) for aa in peptide.split('-')]
    the_spectrum_dict = linear_spectrum(aa_list)
    score = 0
    for s, v in the_spectrum_dict.items():
        v0 = spectrum_dict.get(s, 0)
        if v0 >= v:
            score += v
        else:
            score += v0
    return score

def trim_leaderboard(leaderboard, spectrum_dict, N):
    l = len(leaderboard)
    linear_score_dict = dict()
    for peptide in leaderboard:
        linear_score_dict[peptide] = linear_score(peptide, spectrum_dict)
    lbScore = sorted(linear_score_dict.items(), key=lambda a: a[1], reverse=True)
    leaderboard = [p[0] for p in lbScore]
    linear_scores = [p[1] for p in lbScore]
    for j in range(N, l):
        if linear_scores[j] < linear_scores[N - 1]:
            return leaderboard[:j]
    return leaderboard

def linear_spectrum(aa_list):
    n = len(aa_list)
    prefix_mass = [0]
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + aa_list[i])
    linear_spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
    current_spectrum_dict = dict()
    for s in linear_spectrum:
        current_spectrum_dict[s] = current_spectrum_dict.get(s, 0) + 1
    return current_spectrum_dict

def cyclo_spectrum(aa_list):
    n = len(aa_list)
    prefix_mass = [0]
    for i in range(n):
        prefix_mass.append(prefix_mass[i] + aa_list[i])
    peptide_mass = prefix_mass[n]
    cyclo_spectrum = [0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            cyclo_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                cyclo_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    current_spectrum_dict = dict()
    for s in cyclo_spectrum:
        current_spectrum_dict[s] = current_spectrum_dict.get(s, 0) + 1
    return current_spectrum_dict

def cyclo_score(peptide, spectrum_dict):
    if 0 == len(peptide):
        return 0
    aa_list = [int(aa) for aa in peptide.split('-')]
    the_spectrum_dict = cyclo_spectrum(aa_list)
    score = 0
    for s, v in the_spectrum_dict.items():
        v0 = spectrum_dict.get(s, 0)
        if v0 >= v:
            score += v
        else:
            score += v0
    return score

def is_consistent(self, peptide):
    aa_list = [int(aa) for aa in peptide.split('-')]
    current_spectrum_dict = self.linear_spectrum(aa_list)
    for key, value in current_spectrum_dict.items():
        return value <= self.spectrum_dict.get(key, 0)
    return True

def consistentcyclo_spectrum(peptide):
    aa_list = [int(aa) for aa in peptide.split('-')]
    return cyclo_spectrum(aa_list) == spectrum_dict

def mass_calculate(peptide):
    return sum([int(aa) for aa in peptide.split('-')])

def sequence_calculate():
    peptides = {''}
    result = []
    while len(peptides) > 0:
        peptides = expand(peptides)
        deletions = []
        for peptide in peptides:
            if mass_calculate(peptide) == parent_mass:
                if consistentcyclo_spectrum(peptide):
                    result.append(peptide)
                deletions.append(peptide)
            elif not is_consistent(peptide):
                deletions.append(peptide)
        for p in deletions:
            peptides.remove(p)
    return result

def aa_mass():
    mass = '57 71 87 97 99 101 103 113 114 115 128 129 131 137 147 156 163 186'
    return mass.split()

def expand(peptides):
    mass = aa_mass()
    expanded_peptides = set()
    for p in peptides:
        if '' == p:
            for m in mass:
                expanded_peptides.add(m)
        else:
            for m in mass:
                expanded_peptides.add(p + '-' + m)
    return expanded_peptides

def calculate_sequence_list(spectrum_dict, N):
    leaderboard = {''}
    leaderpeptide = ['']
    bestScore = 0
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        deletions = []
        for peptide in leaderboard:
            if mass_calculate(peptide) == parent_mass:
                current_score = cyclo_score(peptide, spectrum_dict)
                if current_score > bestScore:
                    leaderpeptide = [peptide]
                    bestScore = current_score
            elif mass_calculate(peptide) > parent_mass:
                deletions.append(peptide)
        for p in deletions:
            leaderboard.remove(p)
        leaderboard = trim_leaderboard(leaderboard, spectrum_dict, N)
    return leaderpeptide

N = int(input())
data = list(map(int, input().split()))
spectrum_dict = dict()
for s in data:
    spectrum_dict[s] = spectrum_dict.get(s, 0) + 1
parent_mass = max(spectrum_dict)
result = calculate_sequence_list(spectrum_dict, N)
print(*result)
