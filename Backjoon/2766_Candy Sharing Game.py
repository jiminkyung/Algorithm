# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2766
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    def game(N: int) -> tuple[int, int]:
        candy = [int(input()) for _ in range(N)]
        # 최대캔디와 최소캔디가 일치할때까지 게임 진행
        max_candy = max(candy)
        min_candy = min(candy)
        turn = 0

        while max_candy != min_candy:
            # 나누어 줄 캔디 (= 나누어주고 남은 캔디)
            half = [c//2 for c in candy]

            for i in range(N):
                # 0번째 사람은 i-1 = -1이므로 마지막 사람에게 받음
                candy[i] = half[i] + half[i-1]
                # 나누어주고 나눔받은 후 홀수개라면 한개 추가
                if candy[i] % 2:
                    candy[i] += 1
            
            max_candy = max(candy)
            min_candy = min(candy)

            turn += 1
        
        return turn, max_candy


    while True:
        N = int(input())

        if N == 0:
            break

        print(*game(N))


main()