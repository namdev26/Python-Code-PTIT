import math

def demUoc(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                cnt += 1
            else:
                cnt += 2
    return cnt

def phanNguyenTo():
    results = []
    max_divisors = 0
    for i in range(1, 10000):
        divisors = demUoc(i)
        if divisors > max_divisors:
            max_divisors = divisors
            results.append(i)
    return results

results = phanNguyenTo()

t = int(input())
for _ in range(t):
    x = int(input())
    for num in results:
        if num >= x:
            print(num)
            break
