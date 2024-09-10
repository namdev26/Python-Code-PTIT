t = int(input())
while (t> 0):
    data = input()
    for i in range(len(data)):
        if (data[i].isalpha()):
            res = data[i]
            print(res,end='')
        if (data[i].isdigit()):
            num = int(data[i])
            for i in range(1,num ,1):
                print(res,end="")
    print()
    t-= 1