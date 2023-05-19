def solution(ingredient):
    new_list = []
    answer = 0
    for i in ingredient:
        new_list.append(i)
        if new_list[-4:] == [1, 2, 3, 1]:
            answer += 1
            del new_list[-4:]
    return answer