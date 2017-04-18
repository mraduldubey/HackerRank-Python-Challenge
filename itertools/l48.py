from itertools import combinations_with_replacement
a,b = raw_input().split()
a = sorted(a)
b = int(b)
for each in list(combinations_with_replacement(a,b)):
    res = ""
    for ch in each:
        res += ch
    print res
    
"""
Sample Input

HACK 2

Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""