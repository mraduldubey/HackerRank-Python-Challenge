from collections import Counter

X = int(raw_input().strip())
count_shoes = Counter(map(int,raw_input().split()))
N = int(raw_input().strip())

salary = 0

for _ in xrange(N):
    size, rate = map(int,raw_input().split())
    if count_shoes[size]:
        salary += rate
        count_shoes[size] -= 1

print salary
