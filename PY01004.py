def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

test = int(input())
for _ in range(test):
    n = int(input())
    cnt = 0
    for i in range(1, n + 1): 
        if n % i == 0:
            cnt += 1
    if is_prime(cnt):
        print("YES")
    else:
        print("NO")
