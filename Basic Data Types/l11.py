#List Comprehensions
import itertools
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    thelist = [[i,j,k] for i,j,k in itertools.product(xrange(x+1),xrange(y+1),xrange(z+1)) if i+j+k != n]
    print thelist
    #print x,y,z,n
