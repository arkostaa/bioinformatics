def longest_subsequence(s, t):
    m, n = len(s), len(t)
    arr = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + s[i - 1]
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1], key=len)

    return arr[m][n]

s = input()
t = input()
print(longest_subsequence(s, t))