from itertools import groupby
L = map(int,list(raw_input()))
grouped_L = [(sum(1 for i in g), k) for k,g in groupby(L)]
for each in grouped_L:
    print each,
'''
Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)
'''