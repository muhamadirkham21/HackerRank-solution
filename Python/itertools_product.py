from itertools import product

a = map(int, input().split())
b = map(int, input().split())

res = product(a, b)
for i in res:
    print(i, end=' ')