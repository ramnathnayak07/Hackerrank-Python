n = int(input())
stamps = set()
while n > 0:
    stamps.add(input())
    n -= 1
print(len(stamps))
