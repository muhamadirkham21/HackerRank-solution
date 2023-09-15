n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

total = 0

for i in arr:
    if i in A:
        total += 1
    elif i in B:
        total -= 1

print(total)