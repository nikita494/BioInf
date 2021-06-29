#http://rosalind.info/problems/kmer/
import itertools as it
from Bio import SeqIO
alphabet = 'ACGT'
s = str(next(SeqIO.parse(input(), 'fasta')).seq)
k_mers = {j: 0 for j in map(lambda x: ''.join(x), it.product(*([alphabet] * len(alphabet))))}
for i in range(len(s) - 3):
    k_mers[s[i:i + len(alphabet)]] += 1
print(*[k_mers[i] for i in k_mers.keys()])
