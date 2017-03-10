#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    integer_t  = tuple(integer_list) 
    print hash(integer_t)
