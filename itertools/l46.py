#itertools.permutations()
from itertools import permutations
a,b = raw_input().split()
b = int(b)
for each in list(sorted(permutations(a,b))):
    res = ""
    for ind in xrange(b):
        res += each[ind]
    print res