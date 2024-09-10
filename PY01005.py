inPut = input()

count_4 = 0
count_7 = 0

count_4 = count_4 + inPut.count("4")
count_7 = count_7 + inPut.count("7")

if count_4 + count_7 == 4 or count_7 + count_4 == 7:
    print("YES")
else :
    print("NO")