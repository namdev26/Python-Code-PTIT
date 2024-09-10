def round_number(n):
    a = 10
    while n > a:
        soDu = n % a
        soSanh = a // 2
        if soDu >= soSanh:
            n = n + a - soDu
        else :
            n = n -soDu
        a = a * 10
    return n

num_tests = int(input())
for _ in range(num_tests):
    N = int(input())
    print(round_number(N))