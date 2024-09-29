import math
t = int(input())
while t > 0:
    data = input()
    sum = 0;
    for i in range (0, len(data)):
        sum = sum + math.factorial(int(data[i]))
    if (int(sum) == int(data)):
        print("Yes")
    else:
        print("No")
    t = t - 1