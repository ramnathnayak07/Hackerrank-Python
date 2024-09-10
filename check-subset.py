t = int(input())
while t > 0:
    n = int(input())
    a = set(map(int,input().split()))
    input()
    b = set(map(int,input().split()))
    print(len(a.intersection(b))==n)
    t -= 1