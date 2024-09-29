import math


def checkNguyenTo(s):
    n = int(s)
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True


t = int(input())
while t > 0:
    data = input()
    data2 = data[::-1]
    sum = 0
    ok = 2
    for i in range(len(data)):
        sum = sum + int(data[i])
    for i in range(len(data)):
        if checkNguyenTo(data[i]):
            ok = 1
        else:
            ok = 0
            break
    if checkNguyenTo(data) and checkNguyenTo(data2) and checkNguyenTo(sum) and ok == 1:
        print("Yes")
    else:
        print("No")
    t -= 1
