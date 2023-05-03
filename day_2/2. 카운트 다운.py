def solution(start, end):
    list = []
    for i in range(end, start + 1):
        list.append(i)
    list.reverse()
    return list

test_1 = 10
test_2 = 3

print(solution(test_1, test_2))