import re
from textwrap import wrap
CODON_TABLE = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
               'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
               'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
               'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
               'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
               'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
               'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
               'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
               'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
               'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
               'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
               'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
               'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
               'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
               'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
               'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}


def load_fasta(filename):
    with open(filename) as file:
        data = file.read()
    return {i[0]: i[1] for i in zip(map(lambda x: x[1:], re.findall(r'>\w+', data)),
                                    re.findall(r'[ATCG]+', data.replace('\n', '')))}


def get_translation_dna(dna, introns):
    for i in introns:
        dna = dna.replace(i, '')
    return dna


def dna_to_rna(dna):
    return dna.lower().replace('t', 'u').upper()


def rna_to_protein(rna):
    return ''.join(map(lambda x: CODON_TABLE[x], wrap(rna, 3))).removesuffix('Stop')


data = list(load_fasta(input()).values())
print(rna_to_protein(dna_to_rna(get_translation_dna(data[0], data[1:]))))
