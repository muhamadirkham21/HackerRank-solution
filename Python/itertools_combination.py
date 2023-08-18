from itertools import combinations

a, b = input().split(' ')

result = [combinations(''.join(sorted((a))), int(c)) for c in range(1, int(b)+1)]
for res in result:
    for item in res:
        print(''.join(list(item)))