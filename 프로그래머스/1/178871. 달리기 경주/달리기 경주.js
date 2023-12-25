function solution(players, callings) {
    const players_dict = {};

    players.forEach((player, idx) => {
        players_dict[player] = idx;
    });

    callings.forEach((calling) => {
        const currentIdx = players_dict[calling];
        players_dict[calling] -= 1;
        players_dict[players[currentIdx-1]] += 1;
        [players[currentIdx-1], players[currentIdx]] = [players[currentIdx], players[currentIdx-1]];
    });

    return players;
};
