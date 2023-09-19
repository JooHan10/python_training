def solution(keymap, targets):
    answer = []
    dic = {}
    for i in keymap:
        for idx,value in enumerate(i):
            try:
                if dic[value] > idx: dic[value] = idx+1
            except: dic[value] = idx+1

    for i in targets:
        sum=0
        for j in i:
            try: sum+=dic[j]
            except: 
                sum= -1
                break
        answer.append(sum)
    return answer