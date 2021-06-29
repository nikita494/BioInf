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
def get_matchings(s):
    if len(s) <= 1:
        return 1
    return get_matchings(s[1:]) + sum(get_matchings(s[1:i]) * get_matchings(s[i + 1:]) for i in range(1, len(s))
                                      if s[i] == POSSIBLE_EDGES[s[0]])


print(get_matchings(str(next(SeqIO.parse(input(), 'fasta')).seq)) % 1000000)
