from collections import defaultdict

n, m = map( int, raw_input().split() )

d = defaultdict( list )

for i in xrange( 1, n+1 ):
    ch = raw_input().strip()
    d[ch].append(i)

for i in xrange( 1, m+1 ):
    check = raw_input().strip()
    if d.get(check):
        for each in d.get(check):
                print each,
        print
    else:
        print "-1"

        
    