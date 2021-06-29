#http://rosalind.info/problems/aspc/
from scipy.special import comb
n, m = map(int, input().split())
print(sum([comb(n, k, True) for k in range(m, n + 1)]) % 1000000)
