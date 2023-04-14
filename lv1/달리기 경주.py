def solution(players, callings):
    rank = {player: index for index, player in enumerate(players)}

    for i in callings:
        idx = rank[i] # 현재 등수
        pre_idx = idx - 1 #앞에 있는 선수 등수
        players[idx], players[pre_idx] = players[pre_idx], players[idx] # 서로 바꾸기
        rank[players[idx]] = idx
        rank[players[pre_idx]] = pre_idx

    return players