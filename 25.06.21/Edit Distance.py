#http://rosalind.info/problems/edit/
from Bio import SeqIO


def edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[*range(m + 1)], [0] * (m + 1)]
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i % 2][j] = i
            elif s[j - 1] == t[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = (1 + min(dp[(i - 1) % 2][j],
                                        dp[i % 2][j - 1],
                                        dp[(i - 1) % 2][j - 1]))
    return dp[n % 2][m]


s, t = map(lambda x: x.seq, SeqIO.parse(input(), 'fasta'))
print(edit_distance(s, t))
