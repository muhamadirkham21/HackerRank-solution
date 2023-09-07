from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n+1):
    d[input()].append(str(i))

for j in range(m):
    b = input()

    if b in d:
        print(' '.join(d[b]))
    else:
        print(-1)

