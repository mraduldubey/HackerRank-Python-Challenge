def formatted(number):
    width = len(bin(number))-2
    lines =[]
    for n in range(1,number+1):
        line = '{1:>{0}d} {1:>{0}o} {1:{0}X} {1:{0}b}'.format(width,n)
        lines.append(line)
    return lines
    
def main():
    n = int(raw_input().strip())
    for each in formatted(n):
        print each
main()
        