data = input().split()
n = int(data[0])
k = int(data[1])

def ucln(data1,data2):
    a = int(data1)
    b = int(data2)
    if (b == 0):
        return a
    else: 
        return ucln(b, a % b)

def demPhanTu(data):
    cnt = 0
    while (data > 0):
        data = data // 10
        cnt +=1
    return cnt

cnt = 0
for i in range(1,100000,1):
    if (demPhanTu(i) == k):
        if(ucln(i,n) == 1):
            print(i, end=' ')
            cnt +=1
            if(cnt == 10):
                print()
                cnt =0
    