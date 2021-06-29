#http://rosalind.info/problems/cat/
from Bio import SeqIO
POSSIBLE_EDGES = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}


def cached(fun):
    def cached_fun(*args):
        if args not in cached_fun.cache:
            cached_fun.cache[args] = fun(*args)
        return cached_fun.cache[args]
    cached_fun.cache = dict()
    return cached_fun


@cached
def get_matchings(s, m):
    n = m // 2
    if n <= 1:
        return 1
    return sum(get_matchings(s[1:k], k - 1) * get_matchings(s[k + 1:], 2 * n - k - 1)
               for k in range(1, 2 * n, 2) if s[1:k].count("A") == s[1:k].count("U")
               and s[1:k].count("C") == s[1:k].count("G") and POSSIBLE_EDGES[s[0]] == s[k])


rna = str(next(SeqIO.parse(input(), 'fasta')).seq)
print(get_matchings(rna, len(rna)) % 1000000)
