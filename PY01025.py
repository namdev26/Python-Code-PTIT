n = input()
def daoTu(data):
    return data[::-1]

res = ''
data = daoTu(n)
for i in range(0,len(data),1):
    res = res + data[i]
    if (i % 3 == 2 and i != len(data)-1):
        res = res + ","
print(daoTu(res))
    