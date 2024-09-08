from collections import namedtuple
n,studentMarks = int(input()),namedtuple('sM',input().split())
print("%.2f" % (sum([float(s.MARKS) for s in [studentMarks(*input().split()) for _ in range(n)]])/n))