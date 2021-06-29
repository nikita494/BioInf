#http://rosalind.info/problems/lexv/
import itertools as it
alphabet = input().split()
n = int(input())
print(*sorted(set(it.chain(*(map(lambda x: ''.join(x), it.combinations_with_replacement(alphabet * k, k))
                             for k in range(1, n + 1)))), key=lambda x: [alphabet.index(i) for i in x]), sep='\n')
