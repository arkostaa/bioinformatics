# Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.
#      Input: An integer m.
#      Output: The number of linear peptides having integer mass m.
# Sample Input:
#
# 1024
# Sample Output:
#
# 14712706211

n = int(input())
masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
count = [0] * (n + 1)
count[0] = 1
for i in range(57, n + 1):
    for m in masses:
        if (i - m) >= 0:
            count[i] += count[i - m]
print(count[n])