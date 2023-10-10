import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n)]

def dijkstra(graph, start, limit):
    n = len(graph)
    distance = [INF] * n
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for neighbor_index, cost in graph[now]:
            if dist + cost < distance[neighbor_index] and dist + cost <= limit:
                distance[neighbor_index] = dist + cost
                heapq.heappush(q, (distance[neighbor_index], neighbor_index))
    return distance

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1].append((b-1, l))
    graph[b-1].append((a-1, l))

max_items = 0

for i in range(n):
    distances = dijkstra(graph, i, m)
    total_items = sum(items[j] for j in range(n) if distances[j] <= m)
    max_items = max(max_items, total_items)

print(max_items)