t = int(input())
while t > 0:
    data = input()
    isDigit = []
    res = ''
    for i in range(len(data)):
        if (data[i] == '0' or data[i] == '1' or data[i] == '2'or data[i] == '3'or data[i] == '4'or data[i] == '5'or data[i] == '6'or data[i] == '7'or data[i] == '8'or data[i] == '9'):
            res = res + data[i]
        else :
            if len(res) != 0:
                isDigit.append(int(res))
                res = ''
            else:
                res = ''
    if (res):
        isDigit.append(int(res))
    print(min(isDigit))
    t = t - 1    
