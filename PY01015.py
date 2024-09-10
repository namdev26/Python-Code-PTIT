t = int(input())
while (t>0):
    ok =0
    data = input()
    n = len(data)
    for i in range (0,n-1,1):
        if (data[i] > data[i+1]):
            ok = 1
    if ok ==1:
        print("NO")
    else :
        print ("YES")
    t = t- 1