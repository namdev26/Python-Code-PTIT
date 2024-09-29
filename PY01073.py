import itertools

def list_permutations (s):
    next_permutations = itertools.permutations(s)
    sorted_permutations = sorted(''.join(p) for p in next_permutations)
    return sorted_permutations

s = input()

res = list_permutations(s)
print(res[0])
for i in range(1,len(res)):
    if (res[i] != res[i-1]):
        print(res[i])
    else :
        continue