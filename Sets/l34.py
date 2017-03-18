# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
set1 = set(map(int,raw_input().split()))
n2 = input()
for _ in range(n2):
    op,n2len = raw_input().split()
    set2 = set(map(int,raw_input().split()))
    if op == 'intersection_update':
        set1 &= set2
    elif op == 'update':
        set1 |= set2
    elif op == 'symmetric_difference_update':
        set1 ^= set2
    elif op == 'difference_update':
        set1 -= set2

print sum(set1)
    