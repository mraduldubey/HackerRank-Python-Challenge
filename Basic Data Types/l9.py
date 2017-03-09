if __name__ == '__main__':
    N = int(raw_input())
    lists = []
    while N:
        st = raw_input()
        action = str(st.split(" ")[0])
        if action == "insert":
            i,j = map(int,st.split(" ")[1:])
            lists.insert(i,j)
        elif action == "print":
            print lists
        elif action == 'remove':
            i = int(st.split(" ")[1])
            lists.remove(i)
        elif action == 'append':
            i = int(st.split(" ")[1])
            lists.append(i)
        elif action == 'sort':
            lists=sorted(lists)
        elif action == 'pop':
            lists.pop()
        elif action == 'reverse':
            lists.reverse()
        #print lists,action
        N -= 1
            
            
