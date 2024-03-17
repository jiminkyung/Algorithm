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

# 한큐에 해결한 풀이.
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer