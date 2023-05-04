def solution(array):
    dict_1 = {}
    for i in array:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    sorted_check = sorted(dict_1.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_check) > 1:
        if sorted_check[0][1] != sorted_check[1][1]:
            answer = sorted_check[0][0]
        else:
            answer = -1
    else:
        answer = sorted_check[0][0]

    return answer