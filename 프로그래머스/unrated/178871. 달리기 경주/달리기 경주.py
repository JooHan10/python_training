def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    for calling in callings:
        current_idx = player_dict[calling]
        # print(current_idx)
        player_dict[calling] -= 1
        # print(player_dict[calling])
        player_dict[players[current_idx-1]] += 1
        # print(player_dict[players[current_idx-1]])
        players[current_idx-1], players[current_idx] = players[current_idx], players[current_idx-1]
        
    return players