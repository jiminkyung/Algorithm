# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3280
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    cards = list(range(1, N+1))

    D = int(input())
    # 행 수
    row = N // 3
    # cand[카드 번호]: 정답 후보로 지정된 횟수
    cand = {}

    for _ in range(D):
        cmd = input().rstrip()
        col = -1

        if cmd == "first":
            col = 0
        elif cmd == "second":
            col = 1
        else:
            col = 2
        
        # col번째 열에 해당되는 값들을 카운트.
        for c in [cards[col + 3 * i] for i in range(row)]:
            cand[c] = cand.get(c, 0) + 1

        # 1열부터 시작, 각 열들을 차례대로 모아줌.
        new_cards = [cards[i + 3 * j] for i in range(3) for j in range(row)]
        cards = new_cards
    
    max_cnt = max(cand.values())
    # 정답 후보들 추리기
    ret = [key for key, val in cand.items() if val == max_cnt]
    print(*ret)


main()