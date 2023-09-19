from sys import stdin
input = stdin.readline

def bfs():
    queue = []
    queue.append(n)  # 시작 위치 추가
    while queue:
        x = queue.pop(0)  # 큐의 가장 왼쪽 요소를 꺼냄
        if x == k:  # 현재 위치가 목표 위치와 같으면
            print(dist[x])  # 최단 거리를 출력하고
            break

        for j in (x-1, x+1, x*2):  # 현재 위치에서 가능한 이동을 검사
            if 0 <= j <= MAX and not dist[j]:  # 이동한 위치가 범위 내에 있고 아직 방문하지 않았다면
                dist[j] = dist[x] + 1  # 이동한 위치까지의 최단 거리를 갱신하고
                queue.append(j)  # 이동한 위치를 큐에 추가

MAX = 100000
n, k = map(int, input().split())
dist = [0] * (MAX+1)

bfs()  # BFS 탐색 시작