# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1091
# 메모리: 32544KB / 시간: 252ms
from sys import stdin


input = stdin.readline

def main():
    def mixing(cards: list) -> list:
        new_cards = [0] * N

        for i in range(N):
            new_cards[S[i]] = cards[i]
        return new_cards

    N = int(input())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))

    cards = [(i, P[i]) for i in range(N)]  # (카드 번호, 받아야 할 플레이어)
    start_set = cards[:]  # 초기 카드 상태 저장
    turn = 0

    while True:
        flag = True

        for i, (_, num) in enumerate(cards):
            if (i % 3) != num:  # 플레이어는 단 세명뿐이므로 (0, 1, 2)만 가능함
                flag = False
                break
        
        if flag:  # 모든 카드가 의도한대로 나누어졌다면 break
            break

        cards = mixing(cards)

        # 카드를 섞고 난 후 상태가 시작 상태와 같다면, 어떻게해도 해당 플레이어에게 전해줄 수 없음.
        if cards == start_set:
            turn = -1
            break

        turn += 1
    
    print(turn)


main()