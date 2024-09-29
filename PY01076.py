def ucln (n, m):
    a = int (n)
    b = int (m)
    if (b == 0):
        return a
    return ucln (b, a % b)

t = int(input())
while (t > 0):
    a = input()
    b = input()
    print(ucln(a, b))
    t = t - 1   