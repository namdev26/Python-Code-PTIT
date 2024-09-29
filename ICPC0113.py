import math

def checkNguyenTo(s):
    n = int(s)
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


t = int(input())
while t > 0:
    n = int(input())
    res = []
    for i in range(1,n,1):
        s = str(i)
        if (checkNguyenTo(s) and checkNguyenTo(s[::-1]) and s != s[::-1] and (int(s) < n) and int(s[::-1]) < n):
            if (s in res or s[::-1] in res):
                continue
            else:
                res.append(s)
                res.append(s[::-1])
    for i in res :
        print(i, end=" ")
    print()
    t -= 1
