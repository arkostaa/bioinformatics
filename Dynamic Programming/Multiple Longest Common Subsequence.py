def multiple_longest_common_seq(s1, s2, s3):

    arr = [[[0 for k in range(len(s3)+1)] for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    backtrack = [[[0 for k in range(len(s3) + 1)] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            for k in range(1, len(s3) + 1):
                scores = [arr[i - 1][j - 1][k - 1] + int(s1[i - 1] == s2[j - 1] == s3[k - 1]), arr[i - 1][j][k],
                          arr[i][j - 1][k], arr[i][j][k - 1], arr[i - 1][j][k - 1], arr[i][j - 1][k - 1]]
                backtrack[i][j][k], arr[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    align_s1, align_s2, align_s3 = s1, s2, s3

    i, j, k = len(s1), len(s2), len(s3)
    score = arr[i][j][k]

    while i * j * k != 0:
        if backtrack[i][j][k] == 1:
            i -= 1
            align_s2 = insert_indel(align_s2, j)
            align_s3 = insert_indel(align_s3, k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            align_s1 = insert_indel(align_s1, i)
            align_s3 = insert_indel(align_s3, k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            align_s1 = insert_indel(align_s1, i)
            align_s2 = insert_indel(align_s2, j)
        elif backtrack[i][j][k] == 4:
            i -= 1
            j -= 1
            align_s3 = insert_indel(align_s3, k)
        elif backtrack[i][j][k] == 5:
            i -= 1
            k -= 1
            align_s2 = insert_indel(align_s2, j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            align_s1 = insert_indel(align_s1, i)
        else:
            i -= 1
            j -= 1
            k -= 1

    while len(align_s1) != max(len(align_s1), len(align_s2), len(align_s3)):
        align_s1 = insert_indel(align_s1, 0)
    while len(align_s2) != max(len(align_s1), len(align_s2), len(align_s3)):
        align_s2 = insert_indel(align_s2, 0)
    while len(align_s3) != max(len(align_s1), len(align_s2), len(align_s3)):
        align_s3 = insert_indel(align_s3, 0)

    return str(score), align_s1, align_s2, align_s3


s1 = input()
s2 = input()
s3 = input()

score, align_s1, align_s2, align_s3 = multiple_longest_common_seq(s1, s2, s3)
print(score)
print(align_s1)
print(align_s2)
print(align_s3)
