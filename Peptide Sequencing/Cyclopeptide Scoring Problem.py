# Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
#      Input: An amino acid string Peptide and a collection of integers Spectrum.
#      Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
# Sample Input:
#
# NQEL
# 0 99 113 114 128 227 257 299 355 356 370 371 484
# Sample Output:
#
# 11

def CyclopeptideScoring(Peptide, Spectrum):
    theoretical_spectrum = Cyclospectrum(Peptide)
    Score = 0
    for mass in theoretical_spectrum:
        if mass in Spectrum:
            Score += 1
            Spectrum.remove(mass)
    return Score

def Cyclospectrum(Peptide):
    spectrum = [0]
    PrefixMasses = [0]
    for aminoacid in Peptide:
        PrefixMasses.append(PrefixMasses[-1] + AcidMass[aminoacid])
    peptideMass = PrefixMasses[-1]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide)+1):
            spectrum.append(PrefixMasses[j] - PrefixMasses[i])
            if i > 0 and j < len(Peptide):
                spectrum.append(peptideMass - (PrefixMasses[j] - PrefixMasses[i]))
    return sorted(spectrum)

AcidMass = { "G": 57, "A": 71, "S": 87, "P": 97, "V": 99, "T": 101, "C": 103, "I": 113,
    "L": 113, "N": 114, "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131, "H": 137, "F": 147,
    "R": 156, "Y": 163, "W": 186 }

peptide = input()
spectrum = list(map(int, input().split()))

Score = CyclopeptideScoring(peptide, spectrum)
print(Score)
