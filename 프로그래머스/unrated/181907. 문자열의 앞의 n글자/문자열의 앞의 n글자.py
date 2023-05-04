def solution(my_str, n):
    answer = ''
    for i, str in enumerate(my_str):
        if i != n:
            answer += str
        else:
            break
    return answer