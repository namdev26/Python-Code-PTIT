t = int(input())
while t > 0 :
    data = input().split()
    n = int(data[0])
    heSo = int(data[1])
    if (n == 0):
        print(0)
        break
    res = ''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while ( n > 0):
        res = digits[n % heSo] + res
        n = n // heSo
    print(res)
    t = t - 1