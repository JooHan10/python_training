def solution(l, r):
    answer = []
    list_1 = []
    
    for i in range(l, r+1):
        if '0' in str(i) or '5' in str(i):
            list_1.append(i)

    for j in list_1:
        if '1' not in str(j) and '2' not in str(j) and '3' not in str(j) and '4' not in str(j) and '6' not in str(j) and '7' not in str(j) and '8' not in str(j) and '9' not in str(j):
            answer.append(j)
    
    if answer == []:
        answer.append(-1)
    
    return answer