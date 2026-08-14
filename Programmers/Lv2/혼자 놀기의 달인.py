# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/131130


def solution(cards):
    N = len(cards)
    cards = [card-1 for card in cards]

    def check(visited, start):
        visited[start] = True
        curr = start
        cnt = 1

        # 이미 열어놓은 상자에 도달할때까지 반복
        while True:
            nxt = cards[curr]
            if visited[nxt]:
                break

            cnt += 1
            visited[nxt] = True
            curr = nxt
        
        return cnt, visited


    max_cnt = 0

    for i in range(N):
        visited = [False] * N
        cnt_1, visited = check(visited, i)

        # 첫판에 모든 상자를 열었다면 무효.
        if cnt_1 == N:
            continue

        max_cnt_2 = 0

        for j in range(N):
            if not visited[j]:
                new_visited = visited[:]
                cnt_2, _ = check(new_visited, j)
                max_cnt_2 = max(max_cnt_2, cnt_2)
        
        cnt = cnt_1 * max_cnt_2

        if cnt > max_cnt:
            max_cnt = cnt
    
    return max_cnt