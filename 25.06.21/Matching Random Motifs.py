#http://rosalind.info/problems/rstr/
import operator
import functools
n, gc_content = map(float, input().split())
nucleotides_contents = {'G': gc_content / 2, 'C': gc_content / 2,
                        'A': (1 - gc_content) / 2, 'T': (1 - gc_content) / 2}
s = input()
print(1 - (1 - functools.reduce(operator.mul, map(lambda x: nucleotides_contents[x], s))) ** n)
