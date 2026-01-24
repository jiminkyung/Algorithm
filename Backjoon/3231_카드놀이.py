# 구현
# 애드 훅


# 문제: https://www.acmicpc.net/problem/3231
# 메모리: 40120KB / 시간: 68ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    # pos[x]: x번 카드의 위치
    pos = [-1] * (N+1)

    for i, card in enumerate(cards):
        pos[card] = i
    
    clap = 0
    curr = pos[1]

    # curr번 카드가 nxt 카드보다 앞에 있다면 박수 += 1
    for num in range(2, N+1):
        nxt = pos[num]

        if curr > nxt:
            clap += 1

        curr = nxt
    
    print(clap)


main()