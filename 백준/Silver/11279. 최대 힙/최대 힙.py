import sys
import heapq

N = int(input())
max_heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(-1 * heapq.heappop(max_heap))
        except:
            print(0)
    else:
        heapq.heappush(max_heap, -x)