input()
a = set(map(int,input().split()))
input()
b = set(map(int,input().split()))
a_d = a.difference(b)
b_d = b.difference(a)
for i in b_d:
    a_d.add(i)
for i in sorted(a_d):
    print(i)