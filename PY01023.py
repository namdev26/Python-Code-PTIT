import math

t = int(input())

def checkNT(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    for i in range(2,int(math.sqrt(n)),1):
        if (n % i ==0):
            return False
    return True

while t > 0:
    i = 2
    cnt = 0
    data = int(input())
    print(1,end='')
    while (data > 0):
        if not checkNT(i):
            i+=1
            continue
        if (data % i != 0):
            if cnt != 0:
                print(f' * {i}^{cnt}',end="")
            if data < i:
                break
            i+=1
            cnt = 0
        else:
            cnt+=1
            data/=i
    print()
    t = t - 1