def solution(board, moves):
    tmp = list(zip(*board))
    move = sorted(set(moves))
    dic = {}
    for i in range(len(tmp)):
        dic[move[i]] = list(filter(lambda x: x != 0, tmp[i]))
    curr = [0]
    ret = 0
    for m in moves:
        if dic[m]:
            idx = dic[m].pop(0)
        else:
            continue
        if curr and curr[-1] == idx:
            curr.pop()
            ret += 2
            continue
        curr.append(idx)
    return ret