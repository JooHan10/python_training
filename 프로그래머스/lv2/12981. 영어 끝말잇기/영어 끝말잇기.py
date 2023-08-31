def solution(n, words):
    used_words = []
    player, turn = 0,0
    used_words.append(words[0])
    last_letter = words[0][-1]
    
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == last_letter:
            used_words.append(words[i])
            last_letter = words[i][-1]
        else:
            player = (i%n)+1
            turn = (i//n)+1
            break
    
    return [player, turn]