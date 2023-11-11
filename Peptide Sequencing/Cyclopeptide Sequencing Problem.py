# Implement CyclopeptideSequencing (pseudocode reproduced below).
#
#     CyclopeptideSequencing(Spectrum)
#         Peptides ← a set containing only the empty peptide
#         while Peptides is nonempty
#             Peptides ← Expand(Peptides)
#             for each peptide Peptide in Peptides
#                 if Mass(Peptide) = ParentMass(Spectrum)
#                     if Cyclospectrum(Peptide) = Spectrum
#                         output Peptide
#                     remove Peptide from Peptides
#                 else if Peptide is not consistent with Spectrum
#                     remove Peptide from Peptides
# Sample Input:
#
# 0 113 128 186 241 299 314 427
# Sample Output:
#
# 113-128-186 113-186-128 128-113-186 128-186-113 186-113-128 186-128-113

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

def calculate_mass(peptide):
    return sum([int(aa) for aa in peptide.split('-')])

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

def consistent_cyclo_spectrum(peptide, spectrum_dict):
    aa_list = [int(aa) for aa in peptide.split('-')]
    return cyclo_spectrum(aa_list) == spectrum_dict

def is_consistent(peptide, spectrum_dict):
    aa_list = [int(aa) for aa in peptide.split('-')]
    current_spectrum_dict = linear_spectrum(aa_list)
    for key, value in current_spectrum_dict.items():
        if value > spectrum_dict.get(key, 0):
            return False
    return True

def calculate_sequence_list(parent_mass, spectrum_dict):
    peptides = {''}
    result = []
    while len(peptides) > 0:
        peptides = expand(peptides)
        deletions = []
        for peptide in peptides:
            if calculate_mass(peptide) == parent_mass:
                if consistent_cyclo_spectrum(peptide, spectrum_dict):
                    result.append(peptide)
                deletions.append(peptide)
            elif not is_consistent(peptide, spectrum_dict):
                deletions.append(peptide)
        for p in deletions:
            peptides.remove(p)
    return result

data = list(map(int, input().split()))
spectrum_dict = dict()
for s in data:
    spectrum_dict[s] = spectrum_dict.get(s, 0) + 1
parent_mass = max(spectrum_dict)
result = calculate_sequence_list(parent_mass, spectrum_dict)
print(*result)