import math
test_case = int(input())
for i in range(test_case):
    inPut = input().split()
    n = float(inPut[0])
    x = float(inPut[1])
    m = float(inPut[2])
    lai_sau_1_nam = n
    cnt =0
    while (lai_sau_1_nam < m):
        lai_sau_1_nam = lai_sau_1_nam + (lai_sau_1_nam * x)/100
        cnt = cnt + 1
    print(cnt)
    