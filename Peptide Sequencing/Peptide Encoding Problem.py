# Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
#      Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
#      Output: All substrings of Text encoding Peptide (if any such substrings exist).
#
# Note: The solution may contain repeated strings if the same string occurs more than once as a substring of Text and encodes Peptide.
# Sample Input:
#
# ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
# MA
# Sample Output:
#
# ATGGCC
# ATGGCC
# GGCCAT

RNA_table = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'UAA': '', 'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}


def reverse_complement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(pattern))


def translate_RNA(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        amino_acid = RNA_table.get(codon, '')
        if amino_acid:
            protein += amino_acid
        else:
            break
    return protein


def find_encoding_substrings(Text, Peptide):
    k = len(Peptide) * 3
    substrings = []

    def check_pattern(pattern):
        rna_pattern = pattern.replace('T', 'U')
        return translate_RNA(rna_pattern) == Peptide

    dataset = [Text[j:j + k] for j in range(len(Text) - k + 1)]
    reversed_dataset = [reverse_complement(Text[j:j + k]) for j in range(len(Text) - k + 1)]
    extra_data = dataset + reversed_dataset

    for i, pattern in enumerate(extra_data):
        if check_pattern(pattern):
            substrings.append(extra_data[i % len(dataset)])

    return substrings


Text = input()
Peptide = input()

result = find_encoding_substrings(Text, Peptide)
for data in result:
    print(data)