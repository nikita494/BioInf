#http://rosalind.info/problems/corr/
from Bio import SeqIO


def hamming_distance(s1, s2):
    return sum([1 for i in range(len(s1)) if s1[i] != s2[i]])


complements = {
    'A': 'T',
    'C': 'G',
    'T': 'A',
    'G': 'C'
}


def reverse_complement(dna):
    return ''.join(map(lambda x: complements[x], dna[::-1]))


reads = [i.seq for i in SeqIO.parse(input(), 'fasta')]
all_reads = reads + [reverse_complement(i) for i in reads]
correct_reads = list(filter(lambda x: all_reads.count(x) >= 2, reads))
incorrect_reads = list(filter(lambda x: all_reads.count(x) < 2, reads))
for i in incorrect_reads:
    for j in correct_reads:
        if hamming_distance(i, j) == 1 or hamming_distance(reverse_complement(i), j) == 1:
            print(i, j, sep='->')
            break
