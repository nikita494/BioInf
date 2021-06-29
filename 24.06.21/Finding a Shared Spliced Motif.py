#http://rosalind.info/problems/lcsq/
from Bio import SeqIO


def lcs(s, t):
    l = []
    for _ in range(len(s) + 1):
        l.append([0] * (len(t) + 1))
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    m, n, answer = len(s), len(t), ''
    while l[m][n] != 0:
        if l[m][n] == l[m - 1][n]:
            m -= 1
        elif l[m][n] == l[m][n - 1]:
            n -= 1
        else:
            answer += s[m - 1]
            m -= 1
            n -= 1
    return ''.join(list(answer)[::-1])


s1, s2 = map(lambda x: x.seq, SeqIO.parse(input(), 'fasta'))
print(lcs(s1, s2))
