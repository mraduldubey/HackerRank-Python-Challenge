# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_n = int(raw_input().strip())
eng = set(map(int,raw_input().split()))
fren_n = int(raw_input().strip())
fren = map(int,raw_input().split())

print len(eng.intersection(fren)) #intersection of set and list
