#http://rosalind.info/problems/eval/
from functools import reduce
from operator import mul
n, s, a = int(input()), input(), [float(i) for i in input().split()]
nuc_content = [{'A': (1 - i) / 2, 'T': (1 - i) / 2, 'G': i / 2, 'C': i / 2} for i in a]
print(*(round(reduce(mul, (nuc_content[i][j] for j in s)) * (n - len(s) + 1), 3) for i in range(len(a))))
