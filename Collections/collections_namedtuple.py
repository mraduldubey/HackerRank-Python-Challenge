#The collections.namedtuple solution:

from __future__ import division
from collections import namedtuple

N = int(raw_input().strip())
columns = ','.join(raw_input().split())

student = namedtuple('student', columns)

s = 0

for _ in xrange(N):
    inp = raw_input().split()
    details = student(*inp)
    s += int(details.MARKS)
#For float division we have imported __future__ construct.
print s / N


#The 4 lines Challenge solution:

'''

N = int(raw_input().strip())

index = sum([i for i,each in enumerate(raw_input().split()) if each == 'MARKS'])

marks = [ int(raw_input().split()[index]) for _ in xrange(N) ]

print round( float(sum(marks))/float(N), 2 )

'''
