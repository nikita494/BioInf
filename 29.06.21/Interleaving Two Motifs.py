def common_supersequence(s, t):
    m, n, l = len(s), len(t), [[0] * (len(t) + 1)] * (len(s) + 1)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = max(i, j)
            elif s[i - 1] == t[j - 1]:
                l[i][j] = 1 + l[i - 1][j - 1]
            else:
                l[i][j] = 1 + min(l[i - 1][j], l[i][j - 1])
    x, res, i, j = l[m][n], str(), m, n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res, i, j, x = res + s[i - 1], i - 1, j - 1, x - 1
        elif l[i - 1][j] > l[i][j - 1]:
            res, j, x = res + t[j - 1], j - 1, x - 1
        else:
            res, i, x = res + s[i - 1], i - 1, x - 1
    while i > 0:
        res, i, x = res + s[i - 1], i - 1, x - 1
    while j > 0:
        res, j, x = res + t[j - 1], j - 1, x - 1
    return res[::-1]


print(common_supersequence(input(), input()))
