# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
#      Input: An amino acid string Peptide.
#      Output: Cyclospectrum(Peptide).
#
# Note: An obvious approach for solving the Generating Theoretical Spectrum Problem would be to construct a list containing all subpeptides of Peptide, and then find the mass of each subpeptide by adding the integer masses of its constituent amino acids.
# Sample
# Input:
#
# LEQN
# Sample
# Output:
# 0 113 114 128 129 227 242 242 257 355 356 370 371 484

def get_mass(amino_acid):
    mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                  'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    return mass_table[amino_acid]

def cyclic_spectrum(peptide):
    prefix_masses = [0]
    for i in range(len(peptide)):
        prefix_masses.append(prefix_masses[i] + get_mass(peptide[i]))

    peptide_mass = prefix_masses[-1]
    spectrum = [0]

    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            mass = prefix_masses[j] - prefix_masses[i]
            spectrum.append(mass)
            if i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - mass)

    spectrum.sort()
    return spectrum

peptide = input()
spectrum = cyclic_spectrum(peptide)
print(' '.join(map(str, spectrum)))



