input()
s = set(map(int,input().split()))
q = int(input())
while q > 0:
    query = list(map(str,input().split()))
    new = set(map(int,input().split()))
    if query[0] == "intersection_update":
        s.intersection_update(new)
    elif query[0] == "update":
        s.update(new)
    elif query[0] == "symmetric_difference_update":
        s.symmetric_difference_update(new)
    elif query[0] == "difference_update":
        s.difference_update(new)
    q -= 1
print(sum(s))