from itertools import combinations,ifilter

n = int(raw_input().strip())
str = raw_input().split()
k = int(raw_input().strip())

#Tuples for all combinations of k length from elements in str. 
combs = list(combinations(str,k))

count = 0.0

#All tuples having 'a' in combs are filtered and duly counted.
for _ in ifilter(lambda x: 'a' in x, combs):
    count += 1

print round(count / len(combs), 3)