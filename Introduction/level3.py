def wierdness(n):
    if n%2 == 0:
        if 2<=n<=5 or n>20:
            print "Not Weird"
        if 6<=n<=20:
            print "Weird"
    else:
        print "Weird"
            

if __name__ == '__main__':
    n = int(raw_input())
    wierdness(n)
    
