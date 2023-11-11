# Counting Spectrum of the Linear Peptide: How many subpeptides does a linear peptide of given length n have?
# (Include the empty peptide and the entire peptide.)
#      Input: An integer n.
#      Output: The number of subpeptides of a linear peptide of length n.
# Sample Input:
#
# 11004
# Sample Output:
#
# 60549511
def count_subpeptides(n):
    count = 1
    for i in range(1, n + 1):
        count += (n - i + 1)
    return count

n = int(input())

num_subpeptides = count_subpeptides(n)
print(num_subpeptides)