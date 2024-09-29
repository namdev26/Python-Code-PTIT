
t = int(input())

def daoXau(data):
    return data[::-1]

while t > 0:
    data = input()
    ans = daoXau(data)
    ok = 0
    data_int = [ord(c) for c in data]
    ans_int = [ord(c) for c in ans]
    for i in range(len(data)):
        if (abs(data_int[i] - data_int[i-1]) != abs(ans_int[i] - ans_int[i-1])):
            ok = 1
            break
    if ok ==1:
        print("NO")
    else :
        print("YES")
    t = t -1