def solution(hp):
    ants = [5, 3, 1]
    i, cnt = 0, 0
    while hp > 0:
        if hp < ants[i]:
            i += 1
        cnt += (hp // ants[i])
        hp %= ants[i]
    return cnt