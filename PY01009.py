inPut = input()
cnt_thuong = 0
cnt_hoa = 0
for ky_tu in inPut:
    if (ky_tu.isupper()):
        cnt_hoa = cnt_hoa + 1
    if (ky_tu.islower()):
        cnt_thuong = cnt_thuong + 1
if (cnt_hoa > cnt_thuong):
    outPut = inPut.upper()
else:
    outPut = inPut.lower()
print(outPut)    
  