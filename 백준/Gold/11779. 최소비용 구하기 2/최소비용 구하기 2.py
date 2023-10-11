import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [INF] * n
    prev = [-1] * n
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        cost, now = heapq.heappop(min_heap)
        
        if cost > dist[now]:
            continue
        
        for neighbor_index, weight in graph[now]:
            if dist[now] + weight < dist[neighbor_index]:
                dist[neighbor_index] = dist[now] + weight
                prev[neighbor_index] = now
                heapq.heappush(min_heap, (dist[neighbor_index], neighbor_index))

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return dist[end], path

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]
for _ in range(m):
    start, end, bus_cost = map(int, input().split())
    graph[start-1].append((end-1, bus_cost))

start_city, end_city = map(int, input().split())
start_city -= 1
end_city -= 1

min_cost, min_cost_path = dijkstra(graph, start_city, end_city)

print(min_cost)
print(len(min_cost_path))
print(*[x + 1 for x in min_cost_path])