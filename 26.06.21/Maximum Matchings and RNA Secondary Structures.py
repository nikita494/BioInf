#http://rosalind.info/problems/mmch/
from math import factorial as f
from Bio import SeqIO


def get_max_matchings(seq):
    a, u, c, g = seq.count('A'), seq.count('U'), seq.count('C'), seq.count('G')
    return (f(max((a, u))) // f(max(a, u) - min(a, u))) * (f(max((c, g))) // f(max(c, g) - min(c, g)))


rna = str(next(SeqIO.parse(input(), 'fasta')).seq)
print(get_max_matchings(rna))
