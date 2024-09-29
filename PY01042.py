t = int(input())

while t:
    string = input()
    flag = 1

    if not string.isdigit():
        flag = 0
    else:
        for char in string:
            if char not in "012":
                flag = 0
                break

    print("YES") if flag else print("NO")
    t -= 1
