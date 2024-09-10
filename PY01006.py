test_case = int(input())
current_case = 0

while current_case < test_case :
    inPut = input()

    len_text = len(inPut)

    count_4 = 0
    count_7 = 0

    count_4 = count_4 + inPut.count("4")
    count_7 = count_7 + inPut.count("7")

    if count_4 + count_7 == len_text:
        print("YES")
    else : 
        print ("NO")
    current_case = current_case + 1