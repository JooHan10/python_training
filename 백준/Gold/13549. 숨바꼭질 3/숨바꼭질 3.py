import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
graph = [[] for _ in range(100001)]

def dijkstra(graph, start):
    n = len(graph)
    distance = [INF] * n
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist + weight < distance[neighbor]:
                distance[neighbor] = dist + weight
                heapq.heappush(q, (distance[neighbor], neighbor))
    return distance

for i in range(100001):
    if i - 1 >= 0:
        graph[i].append((i - 1, 1))
    if i + 1 <= 100000:
        graph[i].append((i + 1, 1))
    if i * 2 <= 100000:
        graph[i].append((i * 2, 0))

subin_time = dijkstra(graph, N)
sister_time = dijkstra(graph, K)

result = subin_time[K]
print(result)