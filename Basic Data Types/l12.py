#Find the Second Largest Number

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print sorted(set(arr),reverse=True)[1]
   
