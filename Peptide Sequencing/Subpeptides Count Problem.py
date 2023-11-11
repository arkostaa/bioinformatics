# Peptide Encoding Problem: How many subpeptides does a cyclic peptide of length n have?
#      Input: Length of cyclic peptide
#      Output: Number of subpeptides
#
# Sample Input:
#
# 34215
# Sample Output:
#
# 1170632010

len = int(input())
print(len * (len - 1))
