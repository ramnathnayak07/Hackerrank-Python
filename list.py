if __name__ == '__main__':
    N = int(input())
    listt = []
    while N > 0:
        q = list(map(str,input().split()))
        if q[0] == "print":
            print(listt)
        elif q[0] == "insert":
            listt.insert(int(q[1]),int(q[2]))
        elif q[0] == "remove":
            listt.remove(int(q[1]))
        elif q[0] == "append":
            listt.append(int(q[1]))
        elif q[0] == "sort":
            listt.sort()
        elif q[0] == "pop":
            listt.pop()
        elif q[0] == "reverse":
            listt.reverse()
        N -= 1