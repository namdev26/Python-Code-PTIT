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
    cnt = 0;
    n = int(input())
    arrNguyenTo = []
    for i in range(1, n, 1):
        if checkNguyenTo(i):
            arrNguyenTo.append(i)
    for i in range(2,len(arrNguyenTo)):
        if (arrNguyenTo[i] - arrNguyenTo[i-1] == 4 and arrNguyenTo[i-1]- arrNguyenTo[i-2] == 2) or (arrNguyenTo[i] - arrNguyenTo[i-1] == 2 and arrNguyenTo[i-1]- arrNguyenTo[i-2] == 4):
            cnt += 1
    print(cnt)
    t -= 1
