t = int(input())

while t:
    n = int(input())
    sum = 0
    while n > 0:
        sum += 1 / n
        n -= 2
    print("{:.6f}".format(sum))
    t -= 1
