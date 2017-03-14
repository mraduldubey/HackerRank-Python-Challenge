# Enter your code here. Read input from STDIN. Print output to STDOUT

n1 = int(raw_input().strip())
set1 = set(map(int,raw_input().strip().split(" ")))
n2 = int(raw_input().strip())
set2 = set(map(int,raw_input().strip().split(" ")))

final_set = set1.difference(set2).union(set2.difference(set1)) 

result = sorted(list(final_set)) 
for each in result:
    print each 