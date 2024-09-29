def chuanHoa(s):
    while(len(s) % 3 != 0):
        s = '0' + s
    
    res = ''
    for i in range(0, len(s), 3):
        three_bit = s[i:i+3]
        heSo8 = int(three_bit,2)
        res = res + str(heSo8)
    return res

data = input()
print(chuanHoa(data))
    