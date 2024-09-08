from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(1,n+1):
    d[input()].append(i)
for i in range(m):
    temp = input()
    if temp in d:
        print(*d[temp]) 
    else: 
        print(-1)