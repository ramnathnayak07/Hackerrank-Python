from itertools import permutations
s,k = input().split()
result = list(permutations(s,int(k)))
for i in sorted(result):
    for x in i:
        print(x,end='')
    print()
