def solution(lottos, win_nums):
    count_0 = 0
    count_win = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            count_win += 1
        elif lotto == 0:
            count_0 += 1
        
    count_max_win = count_win + count_0
    result = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    
    return [result[count_max_win], result[count_win]]