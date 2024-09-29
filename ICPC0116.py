t = int(input())
while t > 0:
    data = input()
    if (data[0] == data[-1]):
        print("YES")
    else:
        print("NO")
    t = t - 1