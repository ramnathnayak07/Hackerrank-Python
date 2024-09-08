from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
if __name__ == '__main__':
    s = input()
    for i in OrderedCounter(sorted(s)).most_common(3):
        print(*i)