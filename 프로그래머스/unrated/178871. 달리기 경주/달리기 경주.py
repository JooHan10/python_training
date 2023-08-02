def solution(players, callings):
    answer = []
    dic1={ player:idx for idx,player in enumerate(players,1)}
    dic2={ idx:player for idx,player in enumerate(players,1)}
    for calling in callings:
        rank = dic1[calling]
        pre_rank = rank-1
        tmp = dic2[pre_rank]
        dic2[pre_rank]=dic2[rank]
        dic2[rank]=tmp
        dic1[dic2[rank]] = rank
        dic1[dic2[pre_rank]] = pre_rank
    for rank in dic2.values():
        answer.append(rank)
    return answer