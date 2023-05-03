# 내 풀이
def solution(my_str, n):
    answer = ''
    for i, str in enumerate(my_str):
        if i != n:
            answer += str
        else:
            break
    return answer

# 다른 사람 풀이 1
def solution(my_string, n):
    return my_string[0:n]

# 다른 사람 풀이 2
def solution(my_string, n):
    answer = ''
    for i in range(n) :
        answer += my_string[i]
    return answer