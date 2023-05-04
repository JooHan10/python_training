def solution(start, end):
    list = []
    for i in range(end, start + 1):
        list.append(i)
    list.reverse()
    return list