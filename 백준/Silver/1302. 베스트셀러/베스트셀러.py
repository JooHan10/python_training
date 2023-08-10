import sys

N = int(input())

title_dict = {}

for _ in range(N):
    title = sys.stdin.readline().rstrip()
    if title in title_dict:
        title_dict[title] += 1
    else:
        title_dict[title] = 1

max_value = max(title_dict.values())

best_seller = []
for key, value in title_dict.items():
    if value == max_value:
        best_seller.append(key)

sorted_best_seller = sorted(best_seller)

print(sorted_best_seller[0])