# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
country = set()
for i in xrange(0,n):
    country.add(raw_input().strip())
print len(country)

    