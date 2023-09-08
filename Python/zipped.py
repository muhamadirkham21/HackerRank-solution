X, N = map(int, input().split())

S = []
total =[]

for i in range(N):
    S.append(map(int, input().split()))
    total += [S[i]]

_total = zip(*total)
for value in _total:
    print(sum(value)/len(value))


