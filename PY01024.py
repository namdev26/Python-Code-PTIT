import math
t = int(input())

def tinhTong(n):
    res = 0
    data = int(n)
    while(data > 0):
        res = res + data % 10
        data = data // 10
    return res

def checkKhoangCach(data):
    for i in range(1,len(data)):
        if (abs(int(data[i]) - int(data[i-1])) != 2):
            return False
    return True
            

while (t > 0):
    data = input()
    if (tinhTong(data) % 10 == 0 and checkKhoangCach(data)):
        print("YES")
    else :
        print("NO")
    t= t - 1