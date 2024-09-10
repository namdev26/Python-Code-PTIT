t = int(input())

while t > 0:
    data = input()
    res = ''
    cnt = 1
    for i in range(1,len(data)):
        if (data[i] == data[i-1]):
            cnt = cnt + 1
        else :
            res = res + str(cnt) + data[i-1]
            cnt = 1
    res += str(cnt) + data[-1]      
    print(res)
    t= t - 1