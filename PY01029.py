import math
t = int(input())

def ucln(n,m):
    a = int(n)
    b = int (m)
    if (b==0):
        return a
    else:
        return(ucln(b, a % b))
    

while (t > 0):
    a = input()
    b = a[::-1]
    if (ucln(a,b)==1):
        print("YES")
    else:
        print("NO")
    t = t - 1