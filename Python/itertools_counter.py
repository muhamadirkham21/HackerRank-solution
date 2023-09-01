from collections import Counter

num_shoes = int(input())

list_sizes = Counter(map(int, input().split()))

num_customers = int(input())
totals_earn = 0

for i in range(num_customers):
    size, purchase = map(int, input().split())
    if size in list_sizes and list_sizes[size] > 0:
        totals_earn += purchase
        list_sizes[size] -= 1

print(totals_earn)

