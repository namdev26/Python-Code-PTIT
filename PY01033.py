import math
from itertools import combinations
def ucln(a,b):
    if b == 0:
        return a
    else :
        return ucln(b, a %b)
    
def nguyenToCungNhau(a , b):
    if(ucln(a,b) == 1):
        return True
    return False


data = input().split()
l = int(data[0])
r = int(data[1])

number = list(range(l,r+1))
res = []

for a , b, c in combinations(number, 3):
    if a < b < c :
        if (nguyenToCungNhau(a,b)) and nguyenToCungNhau(b,c) and nguyenToCungNhau(a,c):
            print(f"({a}, {b}, {c})")
            
        