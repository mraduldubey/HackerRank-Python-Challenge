n = input()
s = set(map(int, raw_input().split()))
tc = int(raw_input().strip())
for _ in range(tc):
    op = raw_input().split()
    if len(op) == 1:
        s.pop()
    elif op[0] == 'remove':
        if int(op[1]) in s:
            s.remove(int(op[1]))
    elif op[0] == 'discard':
        s.discard(int(op[1]))
print sum(s)
