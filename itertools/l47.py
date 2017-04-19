from itertools import combinations
a,b = raw_input().split()
a = sorted(a)
b = int(b)
res = [x for each in xrange(1,b+1) for x in list(combinations(a,each))]
for each in res:
    res = ""
    for ch in each:
        res += ch
    print res

