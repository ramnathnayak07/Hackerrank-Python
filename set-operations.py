n = int(input())
s = set(map(int, input().split()))
query =  int(input())
while query > 0:
    q = list(map(str,input().split()))
    if q[0] == "pop":
        s.pop()
    elif q[0] == "discard":
        s.discard(int(q[1]))
    elif q[0] == "remove":
        s.remove(int(q[1]))
    query -= 1
print(sum(s))