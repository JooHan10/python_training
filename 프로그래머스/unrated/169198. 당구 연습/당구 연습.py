def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        distances = []
        # x좌표 같고 목표 y좌표가 큰 경우를 제외
        if not (ballX == startX and ballY > startY):
            result = (ballX - startX)**2 + (ballY - 2*n+startY)**2
            distances.append(result)
        # x좌표가 같고 목표의 y좌표가 더 작은 경우를 제외
        if not (ballX == startX and ballY < startY):
            result = (ballX - startX)**2 + (ballY + startY)**2
            distances.append(result)
        # y좌표가 같고 목표의 x좌표가 더 작은 경우를 제외
        if not (ballY == startY and ballX < startX):
            result = (ballX + startX)**2 + (ballY - startY)**2
            distances.append(result)
        # y좌표가 같고 목표의 x좌표가 더 큰 경우를 제외
        if not (ballY == startY and ballX > startX):
            result = (ballX - 2*m+startX)**2 + (ballY - startY)**2
            distances.append(result)
        answer.append(min(distances))
    return answer