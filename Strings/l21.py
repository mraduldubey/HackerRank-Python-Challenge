#Replace all ______ with rjust, ljust or center. 
'''
thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).rjust(thickness*2)+(c*thickness).ljust(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).rjust(thickness*2)+(c*thickness).ljust(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).center(thickness*6) ''' 
    
from __future__ import print_function, division

char = 'H'
space = ' '

def aligntext(width):
    lines = []
    for n in range(width):
        lines.append((char*(n*2+1)).center(width*2-1, space))

    offset = space*(width*4 - (width*2-1))

    for n in range(width+1):
        lines.append((char*width).center(width*2-1, space) + offset + (char*width).center(width*2-1, space))

    for n in range((width+1)//2):
        lines.append((char*width*5).center(width*6, space))

    for n in range(width+1):
        lines.append((char*width).center(width*2-1, space) + offset + (char*width).center(width*2-1, space))

    for n in reversed(range(width)):
        lines.append(space*(width*4) + (char*(n*2+1)).center(width*2-1, space))

    return lines

def main():
    W = int(input())
    print('\n'.join(aligntext(W)))

if __name__ == '__main__':
    main()
