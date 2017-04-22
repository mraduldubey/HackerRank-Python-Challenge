from itertools import product

K,M = map(int,raw_input().split())
arr=[]
for _ in xrange(K):
    arr.append(map(int,raw_input().split())[1:])

S_max = 0

#We need 1 element from each list, so itertools.product(for all lists)
for each in product(*arr):
    s = sum([x**2 for x in each]) % M
    
    if s>S_max:
        S_max = s

print S_max

    