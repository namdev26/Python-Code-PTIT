t = int(input())
while(t > 0):
    data = input().split()
    d1 = float(data[0])
    d2 = float(data[1])
    d3 = float(data[2])
    d4 = float(data[3])
    read = 0
    lis = 0
    if (d1 >= 3 and d1 <= 4):
        read = 2.5
    elif (d1 >= 5 and d1 <= 6):
        read = 3.0
    elif (d1 >= 7 and d1 <= 9):
        read = 3.5
    elif (d1 >= 10 and d1 <= 12):
        read = 4.0
    elif (d1 >= 13 and d1 <= 15):
        read = 4.5
    elif (d1 >= 16 and d1 <= 19):
        read = 5.0
    elif (d1 >= 20 and d1 <= 22):
        read = 5.5
    elif (d1 >= 23 and d1 <= 26):
        read = 6.0
    elif (d1 >= 27 and d1 <= 29):
        read = 6.5
    elif (d1 >= 30 and d1 <= 32):
        read = 7.0
    elif (d1 >= 33 and d1 <= 34):
        read = 7.5
    elif (d1 >= 35 and d1 <= 36):
        read = 8.0
    elif (d1 >= 37 and d1 <= 38):
        read = 8.5
    elif (d1 >= 39 and d1 <= 40):
        read = 9.0
    
    if (d2 >= 3 and d2 <= 4):
        lis = 2.5
    elif (d2 >= 5 and d2 <= 6):
        lis = 3.0
    elif (d2 >= 7 and d2 <= 9):
        lis = 3.5
    elif (d2 >= 10 and d2 <= 12):
        lis = 4.0
    elif (d2 >= 13 and d2 <= 15):
        lis = 4.5
    elif (d2 >= 16 and d2 <= 19):
        lis = 5.0
    elif (d2 >= 20 and d2 <= 22):
        lis = 5.5
    elif (d2 >= 23 and d2 <= 26):
        lis = 6.0
    elif (d2 >= 27 and d2 <= 29):
        lis = 6.5
    elif (d2 >= 30 and d2 <= 32):
        lis = 7.0
    elif (d2 >= 33 and d2 <= 34):
        lis = 7.5
    elif (d2 >= 35 and d2 <= 36):
        lis = 8.0
    elif (d2 >= 37 and d2 <= 38):
        lis = 8.5
    elif (d2 >= 39 and d2 <= 40):
        lis = 9.0
    ans = (read + lis + d3 + d4)/4
    
    check = ans - int(ans)
    point = 0
    if (check < 0.25 and check >= 0):
        point = 0
    if (check >= 0.75):
        point = 1
    if ( 0.25 <= check < 0.75):
        point = 0.5
    print("{:.1f}".format(int(ans)+ point))
    t = t - 1
    