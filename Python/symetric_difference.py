i = int(input())
M = set(list(map(int, input().split())))

j = int(input())
N = set(list(map(int, input().split())))

uni_ = M.union(N)
inter_ = M.intersection(N)
res = uni_.difference(inter_)

for i in sorted(list(res)):
    print(i)
