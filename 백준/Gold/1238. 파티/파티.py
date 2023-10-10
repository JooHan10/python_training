import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start_point, end_point, cost = map(int, input().split())
    graph[start_point].append((end_point, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X] + back[i])

print(result)