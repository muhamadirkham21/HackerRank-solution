from itertools import permutations

a, b = input().split(' ')
result = sorted(list(permutations(str(a), int(b))))

for res in result:
    print(''.join(list(res)))