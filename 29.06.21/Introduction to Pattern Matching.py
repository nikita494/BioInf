#http://rosalind.info/problems/trie/
import sys


class Trie:
    def __init__(self, sequences=None):
        self.n = 1
        self.root = (self.n, dict())
        self.adjacency_list = list()
        for i in sequences:
            self.add_string(i)

    def add_string(self, seq):
        node = self.root
        for key in seq:
            if key not in node[1]:
                self.n += 1
                node[1][key] = (self.n, dict())
                self.adjacency_list.append((node[0], self.n, key))
            node = node[1][key]


print(*map(lambda x: ' '.join(map(str, x)),
           Trie(map(str.strip, sys.stdin.readlines())).adjacency_list), sep='\n')
