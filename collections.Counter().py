import collections
input()
shoes = list(map(int,input().split()))
shoesCollection = collections.Counter(shoes)
sale = 0
for i in range(int(input())):
    s,n = map(int,input().split())
    if shoesCollection[s] > 0:
        sale += n
        shoesCollection[s] -= 1
print(sale)