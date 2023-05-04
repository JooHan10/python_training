a = [4, 5, 6, 7, 8, 9, 10, 11, 12]
n = 3


def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer_num = i
            answer.append(answer_num)
    return answer


print(solution(n, a))