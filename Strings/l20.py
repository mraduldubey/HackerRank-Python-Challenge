if __name__ == '__main__':
    s = raw_input()
    print any( (c.isalnum() for c in s) ) #called expression generators prefered over list comprehension with any()
    print any( (c.isalpha() for c in s) ) #because any() breaks out earlier
    print any( (c.isdigit() for c in s) )
    print any( (c.islower() for c in s) )
    print any( (c.isupper() for c in s) )
    
        
