# 구현  # 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1680

# 🚨문제 지문에 실수가 있음. "x_i가 작은 지점부터 순서대로 입력이 주어진다."고 되어있지만 실제로는 아님.
# 따라서 중간에 정렬 처리를 하게되면 값 순서에 변화가 생겨버려 틀림.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        W, N = map(int, input().split())
        lst = [tuple(map(int, input().split())) for _ in range(N)]
        
        # 가는 거리 + 되돌아오는 거리 미리 계산
        total = lst[-1][0] * 2
        curr = 0

        for i, (x, w) in enumerate(lst):
            # 1. 쓰레기차의 용량을 넘게 될 때
            if curr + w > W:
                total += x * 2
                curr = 0
            
            curr += w

            # 2. 용량에 도달했을때
            if i != N-1 and curr == W:
                total += x * 2
                curr = 0
            
        print(total)


main()