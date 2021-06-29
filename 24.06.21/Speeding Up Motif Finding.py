#http://rosalind.info/problems/kmp/
from Bio import SeqIO


def fail_table(s):
    fail_arr = [0]
    for i in range(0, len(s)):
        j = i
        while True:
            if j == 0:
                fail_arr.append(0)
                break
            if s[fail_arr[j]] == s[i]:
                fail_arr.append(fail_arr[j] + 1)
                break
            j = fail_arr[j]
    return fail_arr[1:]


s = str(next(SeqIO.parse(input(), 'fasta')).seq)
print(*fail_table(s))
