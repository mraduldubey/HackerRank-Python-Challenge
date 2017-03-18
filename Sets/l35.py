#Good
n = int(raw_input().strip())
rooms = map(int,raw_input().split())
roomset = set(rooms)

print (sum(roomset) * n - sum(rooms)) / (n-1)
