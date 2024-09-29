def tinhMin(a, b, x1, x2):
    n = int (a)
    m = int (b)
    soNho = min(n, m)
    soLon = max(n, m)
    x1 = x1.replace(str(soLon), str(soNho))
    x2 = x2.replace(str(soLon), str(soNho))
    return int(x1) + int(x2)

def tinhMax(a, b, x1, x2):
    n = int (a)
    m = int (b)
    soNho = min(n, m)
    soLon = max(n, m)
    x1 = x1.replace(str(soNho), str(soLon))
    x2 = x2.replace(str(soNho), str(soLon))
    return int(x1) + int(x2)

t = int(input())
while t > 0:
    data = input().split()
    n = int(data[0])  
    m = int(data[1]) 
    x1 = input()
    x2 = input()
    print(tinhMin(n, m, x1, x2), end=" ")
    print(tinhMax(n, m, x1, x2))
    t -= 1 
