# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
x,y = map(float,raw_input().strip('j').split('+'))
print ('%.3f') % abs(complex(x,y))
print ('%.3f') % phase(complex(x,y))