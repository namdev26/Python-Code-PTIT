t = int(input())

while t > 0:
    data = input()
    parts = data.split('.')
    ok = True
    if len(parts) == 4:
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                ok = False
                break
    else:
        ok = False

    if ok:
        print("YES")
    else:
        print("NO")
    t -= 1