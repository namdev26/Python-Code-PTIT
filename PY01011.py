def check_chan(n):
    for i in range(len(n)):
        if (int(n[i]) % 2 == 1):
            return False
    return True    

def check_doi_xung(n):
    return n == n[::-1]

test = int(input())
for i in range (test):
    n = input()
    for i in range(10, int(n), 2):
        if (check_chan(str(i)) and check_doi_xung(str(i))):
            print(i, end= ' ')
    print()