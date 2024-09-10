test_case = int(input())
for i in range(test_case):
    n = input()
    kich_thuoc = len(n)
    so_dau = n[0] + n[1]
    so_cuoi = n[kich_thuoc-2] + n[kich_thuoc-1]
    if (so_dau == so_cuoi):
        print ("YES")
    else:
        print ("NO") 