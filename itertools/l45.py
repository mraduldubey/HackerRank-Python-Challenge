import itertools
a = map(int,raw_input().split())
b = map(int,raw_input().split())
for each in list(itertools.product(a,b)):
    print each,