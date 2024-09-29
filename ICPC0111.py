t = int(input())
while t > 0:
    data = input().split()
    n = int(data[0])
    d = int(data[1])
    arr = input().split()
    for i in range(d, len(arr), 1):
        print(arr[i], end=" ")
    for i in range(0, d , 1):
        print(arr[i], end=" ")
    print()
    t -= 1
