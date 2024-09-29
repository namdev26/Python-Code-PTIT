t = int(input())

while (t > 0):
    data = input()
    if (data[len(data)-1] == '6'and data[len(data)-2] == '8'):
        print("YES")
    else:
        print("NO")
    t = t-1