from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    item,price = input().rsplit(None,1)
    d[item] = d.get(item,0) + int(price)
for k, v in d.items():
    print(k,v)