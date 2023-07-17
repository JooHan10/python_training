def solution(keymap, targets):
    answer = []
    for target in targets:
        time = 0
        for character in target:
            idx=101
            for key in keymap:
                if character in key:
                    idx = min(idx, key.find(character)+1)
            if idx == 101:
                answer.append(-1)
                break
            time += idx
        else:
            answer.append(time)
    return answer