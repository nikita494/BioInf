#http://rosalind.info/problems/conv/
s1, s2 = [float(i) for i in input().split()], [float(i) for i in input().split()]
diff = [round(abs(i - j), 5) for i in s1 for j in s2]
print(max(map(lambda x: diff.count(x), diff)), max(diff, key=lambda x: diff.count(x)), sep='\n')
