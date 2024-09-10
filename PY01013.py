import math

def tinhTong (n):
    res = 0
    while (n> 0):
        res = res + (n % 10);
        n = n //  10
    return res   

def checkNT(n):
    if n == 2:
        return True
    if n <= 1:
        return False
    for i in range(2,n,1):
        if (n % i ==0):
            return False
    return True
    
    
t = int(input());
while t >0:
    data = input().split();
    a = int(data[0]);
    b = int(data[1]);
    ans = math.gcd(a,b)
    chuyenDoi = int(ans)
    res = tinhTong(chuyenDoi)
    if checkNT(res):
        print("YES")
    else :
        print("NO")    
    t-=1
    
