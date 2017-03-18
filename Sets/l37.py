A = set(map(int,raw_input().split()))
flag = True
for _ in range(int(raw_input())):
    B = set(map(int,raw_input().split()))
    if not B<A:
        flag = False
    if len(B)>=len(A):
        flag = False
print flag


    
