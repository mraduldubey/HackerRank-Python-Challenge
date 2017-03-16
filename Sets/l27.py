# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,raw_input().strip().split(" "))
arr = map(int,raw_input().strip().split(" "))
set1 = set(map(int,raw_input().strip().split(" ")))
set2 = set(map(int,raw_input().strip().split(" ")))
happiness = 0
for each in arr:
    happiness += 1 if each in set1 else 0
    happiness += -1 if each in set2 else 0
print happiness
    