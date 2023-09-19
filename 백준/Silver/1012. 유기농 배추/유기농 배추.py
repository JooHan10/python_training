from sys import stdin 

input = stdin.readline

dx = [0, 0, 1, -1]  # x축 방향으로의 이동 (상, 하, 우, 좌)
dy = [1, -1, 0, 0]  # y축 방향으로의 이동 (상, 하, 우, 좌)

t = int(input())

def bfs(graph, a, b):
    queue = []
    queue.append((a, b))  # 시작 위치 추가
    graph[a][b] = 0  # 시작 위치를 0으로 표시하여 방문 처리

    while queue:
        x, y = queue.pop(0)  # 큐의 맨 앞에서 요소를 꺼냄

        for i in range(4):  # 상하좌우 4방향에 대해 탐색
            nx = x + dx[i]  # 새로운 x 좌표 계산
            ny = y + dy[i]  # 새로운 y 좌표 계산

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue  # 범위를 벗어나면 스킵

            if graph[nx][ny] == 1:  # 만약 새로운 위치에 배추가 있다면
                graph[nx][ny] = 0  # 해당 위치를 0으로 표시하여 방문 처리
                queue.append((nx, ny))  # 큐에 추가하여 탐색 계속

    return

for _ in range(t):  # 테스트 케이스 개수만큼 반복
    cnt = 0  # 배추흰지렁이의 개수 초기화
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]  # 배추밭을 2D 리스트로 초기화

    for _ in range(k):  # 배추의 개수만큼 반복하여 배추 위치 입력
        x, y = map(int, input().split())
        graph[x][y] = 1  # 배추가 있는 위치를 1로 표시

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:  # 배추가 있는 위치를 찾으면
                bfs(graph, a, b)  # bfs 함수를 호출하여 연결된 배추 찾기
                cnt += 1  # 연결된 배추 영역이 하나 더 있으므로 개수 증가

    print(cnt)