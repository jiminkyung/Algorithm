# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3256

# 현재 시간 기준을 잘 잡아야 함.
# 나중에 다시 풀어볼만한 문제.
# 메모리: 32412KB / 시간: 108ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    seat = [0] * 1001  # seat[i]: i번 행이 비워지는 시각
    max_time = 0

    for _ in range(N):
        R = int(input())

        time = 0
        # 중간 행들 (1 ~ R-1) 통과
        for i in range(1, R):
            time = max(seat[i], time)  # i행 도착 시각 (앞사람 대기)
            seat[i] = max(time + 1, seat[i + 1])  # 🚨 i행 떠나는 시각 (다음 행 대기 고려)
            time = seat[i]  # 다음 행으로 이동
        
        # 목적지 행 R (짐 넣기 5초)
        time = max(seat[R], time)
        seat[R] = time + 5
        max_time = max(seat[R], max_time)
    
    print(max_time)


main()