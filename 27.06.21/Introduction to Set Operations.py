#http://rosalind.info/problems/seto/
n, a, b = int(input()), {int(i) for i in input()[1:-1].split(', ')}, {int(i) for i in input()[1:-1].split(', ')}
u = {*range(1, n + 1)}
print(a.union(b), a.intersection(b), a - b, b - a, u - a, u - b, sep='\n')
